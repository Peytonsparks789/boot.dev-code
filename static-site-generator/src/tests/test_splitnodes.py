import unittest

from src.markdown_processor.splitnodes import split_nodes_delimiter
from src.nodes.textnode import TextNode, TextType


'''
    Test cases for split_nodes_delimiter
    - plaintext node
        - no delimiter returns original plaintext node
        - one pair of delimiters splits into three nodes
        - multiple delimiter pairs split correctly
        - delimiter at beginning of text
        - delimiter at end of text
        - delimiter surrounds entire string
        - unmatched delimiter raises exception
    - non-plaintext node
        - bold node passed through unchanged
        - italic node passed through unchanged
        - code node passed through unchanged
    - multiple nodes
        - plaintext and bold nodes handled together
        - multiple plaintext nodes split independently
'''


class TestSplitNodesDelimiter(unittest.TestCase):

    # --- plaintext node ---

    def test_no_delimiter_returns_original_plaintext_node(self):
        nodes = [
            TextNode("This is plain text", TextType.PLAINTEXT)
        ]

        expected = [
            TextNode("This is plain text", TextType.PLAINTEXT)
        ]

        self.assertEqual(
            split_nodes_delimiter(nodes, "**", TextType.BOLD),
            expected
        )

    def test_one_pair_of_delimiters_splits_into_three_nodes(self):
        nodes = [
            TextNode("This is **bold** text", TextType.PLAINTEXT)
        ]

        expected = [
            TextNode("This is ", TextType.PLAINTEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" text", TextType.PLAINTEXT),
        ]

        self.assertEqual(
            split_nodes_delimiter(nodes, "**", TextType.BOLD),
            expected
        )

    def test_multiple_delimiter_pairs_split_correctly(self):
        nodes = [
            TextNode("This **one** and **two**", TextType.PLAINTEXT)
        ]

        expected = [
            TextNode("This ", TextType.PLAINTEXT),
            TextNode("one", TextType.BOLD),
            TextNode(" and ", TextType.PLAINTEXT),
            TextNode("two", TextType.BOLD),
            TextNode("", TextType.PLAINTEXT),
        ]

        self.assertEqual(
            split_nodes_delimiter(nodes, "**", TextType.BOLD),
            expected
        )

    def test_delimiter_at_beginning_of_text(self):
        nodes = [
            TextNode("**bold** text", TextType.PLAINTEXT)
        ]

        expected = [
            TextNode("", TextType.PLAINTEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" text", TextType.PLAINTEXT),
        ]

        self.assertEqual(
            split_nodes_delimiter(nodes, "**", TextType.BOLD),
            expected
        )

    def test_delimiter_at_end_of_text(self):
        nodes = [
            TextNode("Text **bold**", TextType.PLAINTEXT)
        ]

        expected = [
            TextNode("Text ", TextType.PLAINTEXT),
            TextNode("bold", TextType.BOLD),
            TextNode("", TextType.PLAINTEXT),
        ]

        self.assertEqual(
            split_nodes_delimiter(nodes, "**", TextType.BOLD),
            expected
        )

    def test_delimiter_surrounds_entire_string(self):
        nodes = [
            TextNode("**bold**", TextType.PLAINTEXT)
        ]

        expected = [
            TextNode("", TextType.PLAINTEXT),
            TextNode("bold", TextType.BOLD),
            TextNode("", TextType.PLAINTEXT),
        ]

        self.assertEqual(
            split_nodes_delimiter(nodes, "**", TextType.BOLD),
            expected
        )

    def test_unmatched_delimiter_raises_exception(self):
        nodes = [
            TextNode("This is **broken markdown", TextType.PLAINTEXT)
        ]

        with self.assertRaises(Exception):
            split_nodes_delimiter(nodes, "**", TextType.BOLD)

    # --- non-plaintext node ---

    def test_bold_node_passed_through_unchanged(self):
        nodes = [
            TextNode("Already bold", TextType.BOLD)
        ]

        self.assertEqual(
            split_nodes_delimiter(nodes, "**", TextType.BOLD),
            nodes
        )

    def test_italic_node_passed_through_unchanged(self):
        nodes = [
            TextNode("Already italic", TextType.ITALIC)
        ]

        self.assertEqual(
            split_nodes_delimiter(nodes, "_", TextType.ITALIC),
            nodes
        )

    def test_code_node_passed_through_unchanged(self):
        nodes = [
            TextNode("print()", TextType.CODE)
        ]

        self.assertEqual(
            split_nodes_delimiter(nodes, "`", TextType.CODE),
            nodes
        )

    # --- multiple nodes ---

    def test_plaintext_and_bold_nodes_processed_together(self):
        nodes = [
            TextNode("Hello **world**", TextType.PLAINTEXT),
            TextNode("Already bold", TextType.BOLD),
        ]

        expected = [
            TextNode("Hello ", TextType.PLAINTEXT),
            TextNode("world", TextType.BOLD),
            TextNode("", TextType.PLAINTEXT),
            TextNode("Already bold", TextType.BOLD),
        ]

        self.assertEqual(
            split_nodes_delimiter(nodes, "**", TextType.BOLD),
            expected
        )

    def test_multiple_plaintext_nodes_split_independently(self):
        nodes = [
            TextNode("**One**", TextType.PLAINTEXT),
            TextNode("**Two**", TextType.PLAINTEXT),
        ]

        expected = [
            TextNode("", TextType.PLAINTEXT),
            TextNode("One", TextType.BOLD),
            TextNode("", TextType.PLAINTEXT),
            TextNode("", TextType.PLAINTEXT),
            TextNode("Two", TextType.BOLD),
            TextNode("", TextType.PLAINTEXT),
        ]

        self.assertEqual(
            split_nodes_delimiter(nodes, "**", TextType.BOLD),
            expected
        )