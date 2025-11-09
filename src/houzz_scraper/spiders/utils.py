"""Utility functions for extracting emails from web pages.

This module provides helper functions for finding and validating email
addresses from HTML content.
"""

import re

import requests
from bs4 import BeautifulSoup


def is_valid_email(email: str) -> bool:
    """Check if a string is a valid email address.

    Args:
        email: The string to validate as an email address.

    Returns:
        True if the email matches the email pattern, False otherwise.
    """
    email_pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b"
    return bool(re.match(email_pattern, email))


def extract_emails(soup: BeautifulSoup) -> list[str]:
    """Extract email addresses from a BeautifulSoup object.

    Searches through various HTML tags to find email addresses and
    validates them before returning.

    Args:
        soup: A BeautifulSoup object to extract emails from.

    Returns:
        A list of unique valid email addresses found in the page.
    """
    email_addresses = set()
    for tag in soup.find_all(["a", "p", "span", "div"]):
        text = tag.get_text()
        for email in re.findall(r"\S+@\S+", text):
            if is_valid_email(email):
                email_addresses.add(email)
    return list(email_addresses)


def extract_emails_from_url(url: str) -> list[str] | str:
    """Extract email addresses from a website URL.

    Fetches the HTML content from the URL and extracts all valid
    email addresses found on the page.

    Args:
        url: The website URL to extract emails from. Should not include
            the protocol (e.g., "example.com" not "https://example.com").

    Returns:
        A list of email addresses if found, empty string if no emails
        found or if the request fails, or None if an exception occurs.
    """
    try:
        response = requests.get(f"https://{url}", timeout=10)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")

            email_addresses = extract_emails(soup)

            if email_addresses:
                return email_addresses
            else:
                return ""
        else:
            return ""

    except Exception as e:
        print(f"An error occurred: {e}")
        return ""
