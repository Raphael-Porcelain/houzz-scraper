#!/usr/bin/env bash
# Simple script to run the Houzz scraper spider

# Set the PYTHONPATH to include the src directory
export PYTHONPATH="${PYTHONPATH:+${PYTHONPATH}:}$(dirname "$0")/../src"

# Run scrapy with the provided arguments (or default to running houzz_scraper)
if [ $# -eq 0 ]; then
    scrapy crawl houzz_scraper
else
    scrapy "$@"
fi
