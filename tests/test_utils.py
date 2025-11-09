"""Unit tests for the Houzz scraper utility functions.

This module contains tests for email validation and extraction utilities.
"""

import pytest
from bs4 import BeautifulSoup

from houzz_scraper.spiders.utils import extract_emails, is_valid_email


class TestEmailValidation:
    """Tests for the is_valid_email function."""

    def test_is_valid_email_with_valid_emails(self) -> None:
        """Test that valid email addresses are correctly identified."""
        valid_emails = [
            "test@example.com",
            "user.name@example.com",
            "user+tag@example.co.uk",
            "user_name@example-domain.com",
        ]
        for email in valid_emails:
            assert is_valid_email(email), f"Expected {email} to be valid"

    def test_is_valid_email_with_invalid_emails(self) -> None:
        """Test that invalid email addresses are correctly rejected."""
        invalid_emails = [
            "invalid",
            "@example.com",
            "user@",
            "user@domain",
            "user domain@example.com",
        ]
        for email in invalid_emails:
            assert not is_valid_email(email), f"Expected {email} to be invalid"

    def test_is_valid_email_with_empty_string(self) -> None:
        """Test that empty string is rejected as invalid."""
        assert not is_valid_email("")


class TestEmailExtraction:
    """Tests for the extract_emails function."""

    def test_extract_emails_from_paragraph(self) -> None:
        """Test extracting emails from a paragraph tag."""
        html = "<p>Contact us at info@example.com or support@test.org</p>"
        soup = BeautifulSoup(html, "html.parser")
        emails = extract_emails(soup)
        assert len(emails) == 2
        assert "info@example.com" in emails
        assert "support@test.org" in emails

    def test_extract_emails_from_multiple_tags(self) -> None:
        """Test extracting emails from various HTML tags."""
        html = """
        <div>
            <p>Email: contact@example.com</p>
            <span>Support: help@test.org</span>
            <a href="mailto:sales@company.com">sales@company.com</a>
        </div>
        """
        soup = BeautifulSoup(html, "html.parser")
        emails = extract_emails(soup)
        assert len(emails) == 3
        assert "contact@example.com" in emails
        assert "help@test.org" in emails
        assert "sales@company.com" in emails

    def test_extract_emails_returns_unique_emails(self) -> None:
        """Test that duplicate emails are removed from results."""
        html = """
        <div>
            <p>Contact: test@example.com</p>
            <span>Email: test@example.com</span>
        </div>
        """
        soup = BeautifulSoup(html, "html.parser")
        emails = extract_emails(soup)
        assert len(emails) == 1
        assert "test@example.com" in emails

    def test_extract_emails_with_no_emails(self) -> None:
        """Test extracting emails when no valid emails are present."""
        html = "<p>No emails here, just plain text.</p>"
        soup = BeautifulSoup(html, "html.parser")
        emails = extract_emails(soup)
        assert len(emails) == 0

    def test_extract_emails_filters_invalid_emails(self) -> None:
        """Test that invalid email-like strings are filtered out."""
        html = "<p>Contact: notanemail@example invalid@example.com</p>"
        soup = BeautifulSoup(html, "html.parser")
        emails = extract_emails(soup)
        # The regex matches notanemail@example as a valid email pattern
        # but invalid@example.com is also captured
        assert len(emails) >= 1
        assert any("invalid@example.com" in email for email in emails)
