"""Scrapy middleware for the Houzz scraper.

This module contains spider and downloader middleware for customizing
the behavior of the Houzz spider.
"""

from typing import Iterator

from itemadapter import ItemAdapter, is_item
from scrapy import signals
from scrapy.http import Request, Response


class HouzzSpiderMiddleware:
    """Spider middleware for the Houzz scraper.

    This middleware can be used to process requests and responses
    at the spider level.
    """

    @classmethod
    def from_crawler(cls, crawler: object) -> "HouzzSpiderMiddleware":  # type: ignore
        """Create middleware instance from crawler.

        Args:
            crawler: The Scrapy crawler object.

        Returns:
            A new instance of HouzzSpiderMiddleware.
        """
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)  # type: ignore
        return s

    def process_spider_input(
        self, response: Response, spider: object
    ) -> None:  # type: ignore
        """Process responses going through the spider.

        Args:
            response: The response being processed.
            spider: The spider processing the response.

        Returns:
            None to continue processing.
        """
        return None

    def process_spider_output(
        self, response: Response, result: Iterator, spider: object  # type: ignore
    ) -> Iterator:  # type: ignore
        """Process the results returned from the spider.

        Args:
            response: The response that generated the results.
            result: An iterator of Request or item objects.
            spider: The spider that generated the results.

        Yields:
            Request or item objects from the result iterator.
        """
        for i in result:
            yield i

    def process_spider_exception(
        self, response: Response, exception: Exception, spider: object
    ) -> None:  # type: ignore
        """Process exceptions raised by the spider.

        Args:
            response: The response being processed when the exception occurred.
            exception: The exception that was raised.
            spider: The spider that raised the exception.

        Returns:
            None to continue exception handling.
        """
        pass

    def process_start_requests(
        self, start_requests: Iterator[Request], spider: object
    ) -> Iterator[Request]:  # type: ignore
        """Process the start requests of the spider.

        Args:
            start_requests: An iterator of start requests.
            spider: The spider generating the requests.

        Yields:
            Request objects from the start_requests iterator.
        """
        for r in start_requests:
            yield r

    def spider_opened(self, spider: object) -> None:  # type: ignore
        """Handle spider opened signal.

        Args:
            spider: The spider that was opened.
        """
        spider.logger.info("Spider opened: %s" % spider.name)  # type: ignore


class HouzzDownloaderMiddleware:
    """Downloader middleware for the Houzz scraper.

    This middleware can be used to process requests and responses
    at the downloader level.
    """

    @classmethod
    def from_crawler(cls, crawler: object) -> "HouzzDownloaderMiddleware":  # type: ignore
        """Create middleware instance from crawler.

        Args:
            crawler: The Scrapy crawler object.

        Returns:
            A new instance of HouzzDownloaderMiddleware.
        """
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)  # type: ignore
        return s

    def process_request(
        self, request: Request, spider: object
    ) -> None:  # type: ignore
        """Process requests going through the downloader.

        Args:
            request: The request being processed.
            spider: The spider making the request.

        Returns:
            None to continue processing the request.
        """
        return None

    def process_response(
        self, request: Request, response: Response, spider: object
    ) -> Response:  # type: ignore
        """Process responses returned from the downloader.

        Args:
            request: The request that generated the response.
            response: The response being processed.
            spider: The spider processing the response.

        Returns:
            The response object.
        """
        return response

    def process_exception(
        self, request: Request, exception: Exception, spider: object
    ) -> None:  # type: ignore
        """Process exceptions raised during request processing.

        Args:
            request: The request being processed when the exception occurred.
            exception: The exception that was raised.
            spider: The spider making the request.

        Returns:
            None to continue exception handling.
        """
        pass

    def spider_opened(self, spider: object) -> None:  # type: ignore
        """Handle spider opened signal.

        Args:
            spider: The spider that was opened.
        """
        spider.logger.info("Spider opened: %s" % spider.name)  # type: ignore
