import unittest

from src.markdown_processor.regex_extractlinks import extract_markdown_links
from src.markdown_processor.regex_extractimages import extract_markdown_images


'''
    Test cases for test_regex.py
    - extract_markdown_images
        - single image extracts alt text and url
        - multiple images extracts all images
        - no images returns empty list
        - image with spaces in alt text extracts properly
    - extract_markdown_links
        - single link extracts text and url
        - multiple links extracts all links
        - no links returns empty list
        - link with spaces in text extracts properly
    - separation
        - image syntax is not extracted as a link
'''


class TestRegexExtractions(unittest.TestCase):

    # --- extract_markdown_images ---

    def test_single_image_extracts_text_and_url(self):
        text = "This is an image ![rick roll](https://image.com/rick.gif)"

        expected = [
            ("rick roll", "https://image.com/rick.gif")
        ]

        self.assertEqual(
            extract_markdown_images(text),
            expected
        )

    def test_multiple_images_extracts_all_images(self):
        text = (
            "![rick roll](https://image.com/rick.gif) "
            "and "
            "![obi wan](https://image.com/obi.jpeg)"
        )

        expected = [
            ("rick roll", "https://image.com/rick.gif"),
            ("obi wan", "https://image.com/obi.jpeg"),
        ]

        self.assertEqual(
            extract_markdown_images(text),
            expected
        )

    def test_no_images_returns_empty_list(self):
        text = "This contains no markdown images"

        expected = []

        self.assertEqual(
            extract_markdown_images(text),
            expected
        )

    def test_image_alt_text_with_spaces_extracts_properly(self):
        text = "![This is my image](https://image.com/test.png)"

        expected = [
            ("This is my image", "https://image.com/test.png")
        ]

        self.assertEqual(
            extract_markdown_images(text),
            expected
        )

    # --- extract_markdown_links ---

    def test_single_link_extracts_text_and_url(self):
        text = "Visit [boot dev](https://www.boot.dev)"

        expected = [
            ("boot dev", "https://www.boot.dev")
        ]

        self.assertEqual(
            extract_markdown_links(text),
            expected
        )

    def test_multiple_links_extracts_all_links(self):
        text = (
            "[boot dev](https://www.boot.dev) "
            "and "
            "[youtube](https://youtube.com)"
        )

        expected = [
            ("boot dev", "https://www.boot.dev"),
            ("youtube", "https://youtube.com"),
        ]

        self.assertEqual(
            extract_markdown_links(text),
            expected
        )

    def test_no_links_returns_empty_list(self):
        text = "This contains no markdown links"

        expected = []

        self.assertEqual(
            extract_markdown_links(text),
            expected
        )

    def test_link_text_with_spaces_extracts_properly(self):
        text = "[Click here to visit](https://example.com)"

        expected = [
            ("Click here to visit", "https://example.com")
        ]

        self.assertEqual(
            extract_markdown_links(text),
            expected
        )

    # --- separation ---

    def test_image_is_not_extracted_as_link(self):
        text = "![rick roll](https://image.com/rick.gif)"

        expected = []

        self.assertEqual(
            extract_markdown_links(text),
            expected
        )