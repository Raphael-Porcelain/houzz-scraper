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

The Houzz scraper can be configured in two ways:

### Option 1: Command-Line Arguments (Recommended)

Run the spider with command-line arguments to specify the starting URL and output options:

```bash
# Set PYTHONPATH to include the src directory
export PYTHONPATH="${PYTHONPATH:+${PYTHONPATH}:}$(pwd)/src"

# Basic usage - scrape a URL and save to default output.csv
scrapy crawl houzz_scraper -a url="https://www.houzz.com/professionals/interior-designer/your-location"

# Customize output file and format
scrapy crawl houzz_scraper \
  -a url="https://www.houzz.com/professionals/..." \
  -a output="results.json" \
  -a format="json"

# Control file overwrite behavior
scrapy crawl houzz_scraper \
  -a url="https://www.houzz.com/professionals/..." \
  -a output="data.csv" \
  -a overwrite="false"
```

**Command-line arguments:**
- `url` (required): Starting URL to scrape
- `output` (optional): Output file path (default: `output.csv`)
- `format` (optional): Output format - `csv` or `json` (default: `csv`)
- `overwrite` (optional): Overwrite existing file - `true` or `false` (default: `true`)

### Option 2: Configuration File

Create a `scraper.conf` file in your project directory:

```bash
# Copy the example configuration file
cp scraper.conf.example scraper.conf

# Edit the configuration file with your settings
nano scraper.conf
```

Example `scraper.conf`:

```ini
[DEFAULT]
start_url = https://www.houzz.com/professionals/interior-designer/your-location
output_file = output.csv
output_format = csv
overwrite = true
```

Then run the spider without arguments:

```bash
export PYTHONPATH="${PYTHONPATH:+${PYTHONPATH}:}$(pwd)/src"
scrapy crawl houzz_scraper
```

**Note:** Command-line arguments override configuration file settings.

### Option 3: Using the Convenience Script

The `run_spider.sh` script simplifies running the scraper:

```bash
# Basic usage
./scripts/run_spider.sh "https://www.houzz.com/professionals/..."

# With all options
./scripts/run_spider.sh "https://www.houzz.com/..." "results.json" "json" "false"
```

Script arguments (in order):
1. Starting URL (required)
2. Output file (optional, default: `output.csv`)
3. Output format (optional, default: `csv`)
4. Overwrite flag (optional, default: `true`)

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
