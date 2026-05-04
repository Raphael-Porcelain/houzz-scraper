"""Spider for scraping business information from Houzz.com.

This module contains the main spider that crawls Houzz.com business listings
and extracts relevant information such as business names, locations, phone
numbers, websites, and email addresses.
"""

import configparser
import time
from collections.abc import Iterator
from pathlib import Path
from typing import Any

import scrapy
from bs4 import BeautifulSoup
from scrapy.http import Response

from houzz_scraper.spiders.utils import extract_emails_from_url


def load_config_file(config_path: str = "scraper.conf") -> dict[str, str]:
    """Load configuration from a config file.

    Args:
        config_path: Path to the configuration file.

    Returns:
        Dictionary containing configuration values.
    """
    config = configparser.ConfigParser()
    config_file = Path(config_path)

    if not config_file.exists():
        return {}

    config.read(config_file)

    # Read from DEFAULT section
    if "DEFAULT" not in config:
        return {}

    return {
        "url": config["DEFAULT"].get("start_url", ""),
        "output": config["DEFAULT"].get("output_file", "output.csv"),
        "format": config["DEFAULT"].get("output_format", "csv"),
        "overwrite": config["DEFAULT"].get("overwrite", "true"),
    }


class HouzzSpider(scrapy.Spider):
    """Spider for scraping Houzz.com business listings.

    This spider crawls through Houzz.com professional listings, extracts
    business information from each listing page, and optionally scrapes
    email addresses from the business websites.

    Configuration can be provided via:
    1. Command-line arguments (highest priority)
    2. Configuration file (scraper.conf)

    Command-line arguments:
        -a url=URL: Starting URL to scrape (required if not in config file)
        -a output=FILE: Output file path (default: output.csv)
        -a format=FORMAT: Output format - csv or json (default: csv)
        -a overwrite=BOOL: Overwrite existing file - true or false (default: true)

    Configuration file (scraper.conf):
        [DEFAULT]
        start_url = https://www.houzz.com/professionals/...
        output_file = output.csv
        output_format = csv
        overwrite = true

    Examples:
        # Using command-line arguments
        scrapy crawl houzz_scraper -a url="https://www.houzz.com/professionals/..."

        # Using configuration file
        scrapy crawl houzz_scraper  # reads from scraper.conf

        # Override config file with command-line
        scrapy crawl houzz_scraper -a output="results.json" -a format="json"

    Attributes:
        name: The name of the spider used by Scrapy.
        base_url: The base URL for Houzz.com.
    """

    name = "houzz_scraper"
    base_url = "https://www.houzz.com"

    def __init__(
        self,
        url: str | None = None,
        output: str | None = None,
        format: str | None = None,  # noqa: A002
        overwrite: str | None = None,
        config: str = "scraper.conf",
        *args: Any,
        **kwargs: Any,
    ) -> None:
        """Initialize the spider and configure settings.

        Configuration priority (highest to lowest):
        1. Command-line arguments
        2. Configuration file
        3. Default values

        Args:
            url: Starting URL to scrape. Required if not in config file.
            output: Output file path. Defaults to "output.csv".
            format: Output format (csv or json). Defaults to "csv".
            overwrite: Whether to overwrite existing file (true/false).
                Defaults to "true".
            config: Path to configuration file. Defaults to "scraper.conf".
            *args: Variable length argument list passed to parent class.
            **kwargs: Arbitrary keyword arguments passed to parent class.

        Raises:
            ValueError: If url is not provided via command-line or config file.
        """
        super().__init__(*args, **kwargs)
        self.start_time = time.time()

        # Load configuration from file if it exists
        config_values = load_config_file(config)

        # Command-line arguments override config file
        final_url = url or config_values.get("url")
        final_output = output or config_values.get("output", "output.csv")
        final_format = format or config_values.get("format", "csv")
        final_overwrite = overwrite or config_values.get("overwrite", "true")

        # Validate required parameters
        if not final_url:
            raise ValueError(
                "Starting URL is required. Provide via:\n"
                "  Command-line: -a url='https://www.houzz.com/...'\n"
                "  Config file: Create scraper.conf with start_url setting"
            )

        self.start_urls = [final_url]

        # Configure output settings
        overwrite_bool = final_overwrite.lower() in ("true", "yes", "1")
        self.custom_settings = {
            "FEEDS": {
                final_output: {
                    "format": final_format.lower(),
                    "overwrite": overwrite_bool,
                },
            }
        }

    def parse(self, response: Response) -> Iterator[scrapy.Request]:
        """Parse the main listing page and extract business links.

        Extracts links to individual business pages and follows pagination
        to the next page of results.

        Args:
            response: The HTTP response from the listing page.

        Yields:
            Request objects for business detail pages and pagination.
        """
        target_elements = response.css("a.hz-pro-ctl::attr(href)").extract()
        for url in target_elements:
            yield response.follow(url, callback=self.parse_subpage)

        next_page = response.css("a.hz-pagination-link--next::attr(href)").get()

        if next_page:
            yield scrapy.Request(self.base_url + next_page, callback=self.parse)

    def parse_subpage(self, response: Response) -> Iterator[dict[str, Any]]:
        """Parse a business detail page and extract information.

        Extracts business information from the business section of the page,
        including name, location, phone, and website. If a website is found,
        attempts to extract email addresses from it.

        Args:
            response: The HTTP response from the business detail page.

        Yields:
            Dictionary containing the scraped business information.
        """
        soup = BeautifulSoup(response.body, "html.parser")
        data: dict[str, Any] = {"url": response.url}

        business_section = soup.find("section", id="business")

        if business_section:
            for div in business_section.find_all("div"):
                h3 = div.find("h3")
                if h3:
                    key = h3.get_text(strip=True)
                    p = div.find("p")
                    if p:
                        value = p.get_text()
                        data[key] = value

        if "Website" in data:
            found_emails = extract_emails_from_url(data["Website"])
            data["Emails"] = found_emails

        yield data

    def closed(self, reason: str) -> None:
        """Handle spider closure and log total execution time.

        Args:
            reason: The reason for spider closure.
        """
        end_time = time.time()
        total_time = end_time - self.start_time
        self.log(f"Total time taken for scraping: {total_time} seconds")
