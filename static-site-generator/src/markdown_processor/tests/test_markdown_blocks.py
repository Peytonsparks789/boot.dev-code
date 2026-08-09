import unittest

from src.markdown_processor.markdown_to_blocks import markdown_to_blocks, block_to_block_type, BlockType

'''
Test cases for test_markdown_to_blocks.py

- markdown_to_blocks
  - single block returns one block
  - multiple blocks returns all blocks
  - leading and trailing whitespace is stripped
  - excessive newlines do not create empty blocks
  - single newlines are preserved within a block
  - markdown formatting is preserved

- block_to_block_type
  - paragraph returns paragraph type
  - heading returns heading type
  - code block returns code type
  - quote returns quote type
  - unordered list returns unordered list type
  - ordered list returns ordered list type
  - ordered list does not require sequential numbers
'''

class TestMarkdownToBlocks(unittest.TestCase):

    # --- markdown_to_blocks ---

    def test_single_block_returns_one_block(self):
        markdown = "# This is a heading"

        expected = [
            "# This is a heading"
        ]

        blocks = markdown_to_blocks(markdown)

        self.assertEqual(
            blocks,
            expected
        )

    def test_multiple_blocks_returns_all_blocks(self):
        markdown = (
            "# This is a heading\n\n"
            "This is a paragraph of text.\n\n"
            "- This is the first list item\n"
            "- This is a list item\n"
            "- This is another list item"
        )

        expected = [
            "# This is a heading",
            "This is a paragraph of text.",
            "- This is the first list item\n"
            "- This is a list item\n"
            "- This is another list item"
        ]

        blocks = markdown_to_blocks(markdown)

        self.assertEqual(
            blocks,
            expected
        )

    def test_leading_and_trailing_whitespace_is_stripped(self):
        markdown = (
            "  \n"
            "  # This is a heading  \n"
            "\n\n"
            "  This is a paragraph.  \n"
            "  "
        )

        expected = [
            "# This is a heading",
            "This is a paragraph."
        ]

        blocks = markdown_to_blocks(markdown)

        self.assertEqual(
            blocks,
            expected
        )

    def test_excessive_newlines_do_not_create_empty_blocks(self):
        markdown = (
            "# This is a heading\n\n\n\n"
            "This is a paragraph.\n\n\n"
            "- This is a list item"
        )

        expected = [
            "# This is a heading",
            "This is a paragraph.",
            "- This is a list item"
        ]

        blocks = markdown_to_blocks(markdown)

        self.assertEqual(
            blocks,
            expected
        )

    def test_single_newlines_are_preserved_within_block(self):
        markdown = (
            "- This is the first list item\n"
            "- This is a list item\n"
            "- This is another list item"
        )

        expected = [
            "- This is the first list item\n"
            "- This is a list item\n"
            "- This is another list item"
        ]

        blocks = markdown_to_blocks(markdown)

        self.assertEqual(
            blocks,
            expected
        )

    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""

        blocks = markdown_to_blocks(md)

        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    # --- block_to_block_type ---

    def test_paragraph_returns_paragraph_type(self):
        block = "This is a paragraph of text."

        self.assertEqual(
            block_to_block_type(block),
            BlockType.PARAGRAPH
        )

    def test_heading_returns_heading_type(self):
        block = "# This is a heading"

        self.assertEqual(
            block_to_block_type(block),
            BlockType.HEADING
        )

    def test_code_block_returns_code_type(self):
        block = "```print('Hello, world!')```"

        self.assertEqual(
            block_to_block_type(block),
            BlockType.CODE
        )

    def test_quote_returns_quote_type(self):
        block = "> This is a quote"

        self.assertEqual(
            block_to_block_type(block),
            BlockType.QUOTE
        )

    def test_unordered_list_returns_unordered_list_type(self):
        block = (
            "- First item\n"
            "- Second item\n"
            "- Third item"
        )

        self.assertEqual(
            block_to_block_type(block),
            BlockType.UNORDERED_LIST
        )

    def test_ordered_list_returns_ordered_list_type(self):
        block = (
            "1. First item\n"
            "2. Second item\n"
            "3. Third item"
        )

        self.assertEqual(
            block_to_block_type(block),
            BlockType.ORDERED_LIST
        )

    def test_ordered_list_does_not_require_sequential_numbers(self):
        block = (
            "1. First item\n"
            "1. Second item\n"
            "7. Third item"
        )

        self.assertEqual(
            block_to_block_type(block),
            BlockType.ORDERED_LIST
        )