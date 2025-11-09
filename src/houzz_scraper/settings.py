"""Scrapy settings for the Houzz scraper project.

This module contains the configuration settings for the Houzz scraper spider.
For more information about Scrapy settings see:
https://docs.scrapy.org/en/latest/topics/settings.html
"""

BOT_NAME = "houzz_scraper"

SPIDER_MODULES = ["houzz_scraper.spiders"]
NEWSPIDER_MODULE = "houzz_scraper.spiders"

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Configure default feed export settings
FEED_FORMAT = "json"
FEED_URI = "output.json"
FEED_EXPORT_ENCODING = "utf-8"

# Scrapy version compatibility settings
REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
