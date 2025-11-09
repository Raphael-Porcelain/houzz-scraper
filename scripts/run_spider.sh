#!/usr/bin/env bash
# Script to run the Houzz scraper spider with configuration options
#
# Usage:
#   ./scripts/run_spider.sh <url> [output_file] [format] [overwrite]
#
# Examples:
#   ./scripts/run_spider.sh "https://www.houzz.com/professionals/..."
#   ./scripts/run_spider.sh "https://www.houzz.com/..." "results.json" "json" "false"

# Set the PYTHONPATH to include the src directory
export PYTHONPATH="${PYTHONPATH:+${PYTHONPATH}:}$(dirname "$0")/../src"

# Check if URL is provided
if [ $# -eq 0 ]; then
    echo "Error: Starting URL is required"
    echo ""
    echo "Usage: $0 <url> [output_file] [format] [overwrite]"
    echo ""
    echo "Arguments:"
    echo "  url          Starting URL to scrape (required)"
    echo "  output_file  Output file path (default: output.csv)"
    echo "  format       Output format: csv or json (default: csv)"
    echo "  overwrite    Overwrite existing file: true or false (default: true)"
    echo ""
    echo "Examples:"
    echo "  $0 'https://www.houzz.com/professionals/interior-designer/...'"
    echo "  $0 'https://www.houzz.com/...' 'results.json' 'json' 'false'"
    exit 1
fi

# Build scrapy command with arguments
URL="$1"
OUTPUT="${2:-output.csv}"
FORMAT="${3:-csv}"
OVERWRITE="${4:-true}"

scrapy crawl houzz_scraper \
    -a "url=$URL" \
    -a "output=$OUTPUT" \
    -a "format=$FORMAT" \
    -a "overwrite=$OVERWRITE"

