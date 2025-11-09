"""Spider for scraping business information from Houzz.com.

This module contains the main spider that crawls Houzz.com business listings
and extracts relevant information such as business names, locations, phone
numbers, websites, and email addresses.
"""

import time
from typing import Any, Iterator

import scrapy
from bs4 import BeautifulSoup
from scrapy.http import Response

from houzz_scraper.spiders.utils import extract_emails_from_url


class HouzzSpider(scrapy.Spider):
    """Spider for scraping Houzz.com business listings.

    This spider crawls through Houzz.com professional listings, extracts
    business information from each listing page, and optionally scrapes
    email addresses from the business websites.

    Attributes:
        name: The name of the spider used by Scrapy.
        base_url: The base URL for Houzz.com.
        start_urls: List of URLs to begin crawling from.
        custom_settings: Spider-specific settings that override project settings.
    """

    name = "houzz_scraper"

    base_url = "https://www.houzz.com"
    start_urls = [
        "https://www.houzz.com/professionals/interior-designer/carter-lake-ia-us-probr0-bo~t_11785~r_4850531"
    ]

    custom_settings = {
        "FEEDS": {
            "output.csv": {
                "format": "csv",
                "overwrite": True,
            },
        }
    }

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Initialize the spider and record start time.

        Args:
            *args: Variable length argument list passed to parent class.
            **kwargs: Arbitrary keyword arguments passed to parent class.
        """
        super(HouzzSpider, self).__init__(*args, **kwargs)
        self.start_time = time.time()

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
