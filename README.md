# Web Scraping with Python: Houzz.com Scraper

## Table of Contents

- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
- [Output](#output)
- [Development](#development)
- [Contributing](#contributing)
- [License](#license)

## Introduction

Welcome to the **Web Scraping with Python: Houzz.com Scraper** project. This repository contains a Python web scraping tool that extracts data from business websites on [www.houzz.com](https://www.houzz.com). The scraper is built on Scrapy and BeautifulSoup and is designed to collect information from business sites on Houzz.com, allowing you to store the data in a CSV file for further analysis or usage.

![Houzz.com](https://github.com/adil6572/houzz-scraper/blob/main/Houzz.png)

## Output

The scraper extracts the following information from Houzz.com business listings:

- **Business Name**: The name of the business
- **Location**: The location of the business
- **Phone Number**: The contact phone number of the business
- **Website URL**: The website URL of the business
- **Email**: Email addresses found on the business website (if available)

## Installation

### Prerequisites

- Python 3.11 or higher
- [uv](https://github.com/astral-sh/uv) package manager (recommended) or pip

### Using uv (Recommended)

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/Raphael-Porcelain/houzz-scraper.git
   cd houzz-scraper
   ```

2. Install dependencies using uv:

   ```bash
   uv sync
   ```

### Using pip

1. Clone this repository:

   ```bash
   git clone https://github.com/Raphael-Porcelain/houzz-scraper.git
   cd houzz-scraper
   ```

2. Install the required Python packages:

   ```bash
   pip install scrapy beautifulsoup4 requests
   ```

## Usage

To use the Houzz.com Scraper, follow these steps:

### Configuring the Spider

To modify the `start_urls` and `custom_settings` in the Houzz.com scraper:

#### Changing `start_urls`:

1. Open the `src/houzz_scraper/spiders/houzz_spider.py` file in your project directory.

2. Locate the `start_urls` variable, which is defined as a list of URLs. You can change the URL to the one you want to scrape.

3. Replace the existing URL with the new URL you want to scrape (the URL should be a Houzz professional listing page). For example:

   ```python
   start_urls = ["https://www.houzz.com/professionals/interior-designer/your-location-here"]
   ```

#### Changing `custom_settings`:

1. In the same `src/houzz_scraper/spiders/houzz_spider.py` file, find the `custom_settings` dictionary.

2. Within the `custom_settings` dictionary, you can customize various settings related to the scraper's behavior:

   - To change the output file format to JSON:

     ```python
     'FEEDS': {
         'output.json': {
             'format': 'json',
             'overwrite': True,  # Set to True to overwrite the file if it already exists
         },
     }
     ```

   - To set the scraper to append data to the existing file instead of overwriting:

     ```python
     'FEEDS': {
         'output.csv': {
             'format': 'csv',
             'overwrite': False,  # Set to False to append data to the existing file
         },
     }
     ```

3. Save the file with your changes.

### Running the Scraper

#### With uv:

```bash
# Set PYTHONPATH to include the src directory
export PYTHONPATH="${PYTHONPATH:+${PYTHONPATH}:}$(pwd)/src"

# Run the spider
uv run scrapy crawl houzz_scraper
```

#### With pip:

```bash
# Set PYTHONPATH to include the src directory
export PYTHONPATH="${PYTHONPATH:+${PYTHONPATH}:}$(pwd)/src"

# Run the spider
scrapy crawl houzz_scraper
```

#### Using the convenience script:

```bash
# The script automatically sets PYTHONPATH
./scripts/run_spider.sh
```

The scraper will begin extracting information from Houzz.com business websites and store it in a CSV file (or your configured output format).

You can now use this data for your intended purposes, such as analysis, data processing, or any other creative project.

## Development

### Setting Up Development Environment

1. Install development dependencies:

   ```bash
   uv sync --group dev
   ```

2. Install pre-commit hooks:

   ```bash
   uv run pre-commit install --hook-type commit-msg --hook-type pre-push
   ```

### Code Quality

Run linting and formatting:

```bash
# Check and fix linting issues
uv run ruff check . --fix

# Format code
uv run ruff format .
```

### Testing

Run tests with coverage:

```bash
uv run pytest --cov=src --cov-report=term-missing
```

### Type Checking

Run type checking:

```bash
uv run mypy src
```

## Contributing

If you'd like to contribute to this project, please follow these steps:

1. Fork the repository to your own GitHub account.

2. Clone the forked repository to your local machine.

3. Create a new branch with a descriptive name for your feature or bug fix:

   ```bash
   git checkout -b feat/your-feature-name
   ```

4. Make your changes following the [contribution guidelines](CONTRIBUTING.md).

5. Ensure all tests pass and code is properly formatted:

   ```bash
   uv run ruff check . --fix
   uv run ruff format .
   uv run pytest
   ```

6. Commit your changes using conventional commits:

   ```bash
   uv run cz commit
   ```

7. Push your branch to your GitHub repository:

   ```bash
   git push origin feat/your-feature-name
   ```

8. Create a pull request to the main repository, explaining your changes and improvements.

We welcome your contributions and ideas to make this project even better! For more details, see [CONTRIBUTING.md](CONTRIBUTING.md).

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Thank you for using the Houzz.com Scraper! Happy web scraping and data extraction! If you have any questions or need assistance, feel free to open an issue or contact the maintainers.
