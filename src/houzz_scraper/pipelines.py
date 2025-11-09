"""Scrapy pipelines for processing scraped items.

This module contains pipelines that can be used to process items
scraped by the Houzz spider.
"""


class HouzzPipeline:
    """Pipeline for processing Houzz scraped items.

    This pipeline can be extended to perform data cleaning, validation,
    or storage operations on scraped items.
    """

    def process_item(self, item: dict, spider: object) -> dict:  # type: ignore[type-arg]
        """Process a scraped item.

        Args:
            item: The scraped item to process.
            spider: The spider that scraped the item.

        Returns:
            The processed item.
        """
        return item
