import unittest

from src.markdown_processor.splitnodes import split_nodes_delimiter, split_nodes_image, split_nodes_links
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

Test cases for split_nodes_image
- single image splits into two nodes
- multiple images split correctly
- image at beginning of text
- image at end of text
- no image returns original plaintext node
- non-plaintext node passed through unchanged
- multiple identical images split correctly

Test cases for split_nodes_links
- single link splits into two nodes
- multiple links split correctly
- link at beginning of text
- link at end of text
- no link returns original plaintext node
- non-plaintext node passed through unchanged
- multiple identical links split correctly
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

    # --- split_nodes_image ---

    def test_single_image_splits_into_two_nodes(self):
        nodes = [
            TextNode(
                "This is an ![image](https://image.com/image.png)",
                TextType.PLAINTEXT
            )
        ]

        expected = [
            TextNode(
                "This is an ",
                TextType.PLAINTEXT
            ),
            TextNode(
                "image",
                TextType.IMAGES,
                "https://image.com/image.png"
            ),
        ]

        self.assertEqual(
            split_nodes_image(nodes),
            expected
        )

    def test_multiple_images_split_correctly(self):
        nodes = [
            TextNode(
                "This is an ![image](https://image.com/image.png)"
                " and another ![second image](https://image.com/second.png)",
                TextType.PLAINTEXT
            )
        ]

        expected = [
            TextNode(
                "This is an ",
                TextType.PLAINTEXT
            ),
            TextNode(
                "image",
                TextType.IMAGES,
                "https://image.com/image.png"
            ),
            TextNode(
                " and another ",
                TextType.PLAINTEXT
            ),
            TextNode(
                "second image",
                TextType.IMAGES,
                "https://image.com/second.png"
            ),
        ]

        self.assertEqual(
            split_nodes_image(nodes),
            expected
        )

    def test_image_at_beginning_of_text(self):
        nodes = [
            TextNode(
                "![image](https://image.com/image.png) comes first",
                TextType.PLAINTEXT
            )
        ]

        expected = [
            TextNode(
                "image",
                TextType.IMAGES,
                "https://image.com/image.png"
            ),
            TextNode(
                " comes first",
                TextType.PLAINTEXT
            ),
        ]

        self.assertEqual(
            split_nodes_image(nodes),
            expected
        )

    def test_image_at_end_of_text(self):
        nodes = [
            TextNode(
                "The image is ![image](https://image.com/image.png)",
                TextType.PLAINTEXT
            )
        ]

        expected = [
            TextNode(
                "The image is ",
                TextType.PLAINTEXT
            ),
            TextNode(
                "image",
                TextType.IMAGES,
                "https://image.com/image.png"
            ),
        ]

        self.assertEqual(
            split_nodes_image(nodes),
            expected
        )

    def test_no_image_returns_original_plaintext_node(self):
        nodes = [
            TextNode(
                "This is plain text",
                TextType.PLAINTEXT
            )
        ]

        expected = [
            TextNode(
                "This is plain text",
                TextType.PLAINTEXT
            )
        ]

        self.assertEqual(
            split_nodes_image(nodes),
            expected
        )

    def test_image_node_preserves_non_plaintext_nodes(self):
        nodes = [
            TextNode(
                "Already bold",
                TextType.BOLD
            )
        ]

        self.assertEqual(
            split_nodes_image(nodes),
            nodes
        )

    def test_multiple_identical_images_split_correctly(self):
        nodes = [
            TextNode(
                "First ![image](https://image.com/image.png)"
                " and second ![image](https://image.com/image.png)",
                TextType.PLAINTEXT
            )
        ]

        expected = [
            TextNode(
                "First ",
                TextType.PLAINTEXT
            ),
            TextNode(
                "image",
                TextType.IMAGES,
                "https://image.com/image.png"
            ),
            TextNode(
                " and second ",
                TextType.PLAINTEXT
            ),
            TextNode(
                "image",
                TextType.IMAGES,
                "https://image.com/image.png"
            ),
        ]

        self.assertEqual(
            split_nodes_image(nodes),
            expected
        )

    # --- split_nodes_links ---

    def test_single_link_splits_into_two_nodes(self):
        nodes = [
            TextNode(
                "This is a [link](https://example.com)",
                TextType.PLAINTEXT
            )
        ]

        expected = [
            TextNode(
                "This is a ",
                TextType.PLAINTEXT
            ),
            TextNode(
                "link",
                TextType.LINK,
                "https://example.com"
            ),
        ]

        self.assertEqual(
            split_nodes_links(nodes),
            expected
        )

    def test_multiple_links_split_correctly(self):
        nodes = [
            TextNode(
                "This is a [link](https://example.com)"
                " and another [link](https://another.com)",
                TextType.PLAINTEXT
            )
        ]

        expected = [
            TextNode(
                "This is a ",
                TextType.PLAINTEXT
            ),
            TextNode(
                "link",
                TextType.LINK,
                "https://example.com"
            ),
            TextNode(
                " and another ",
                TextType.PLAINTEXT
            ),
            TextNode(
                "link",
                TextType.LINK,
                "https://another.com"
            ),
        ]

        self.assertEqual(
            split_nodes_links(nodes),
            expected
        )

    def test_link_at_beginning_of_text(self):
        nodes = [
            TextNode(
                "[link](https://example.com) comes first",
                TextType.PLAINTEXT
            )
        ]

        expected = [
            TextNode(
                "link",
                TextType.LINK,
                "https://example.com"
            ),
            TextNode(
                " comes first",
                TextType.PLAINTEXT
            ),
        ]

        self.assertEqual(
            split_nodes_links(nodes),
            expected
        )

    def test_link_at_end_of_text(self):
        nodes = [
            TextNode(
                "Visit [link](https://example.com)",
                TextType.PLAINTEXT
            )
        ]

        expected = [
            TextNode(
                "Visit ",
                TextType.PLAINTEXT
            ),
            TextNode(
                "link",
                TextType.LINK,
                "https://example.com"
            ),
        ]

        self.assertEqual(
            split_nodes_links(nodes),
            expected
        )

    def test_no_link_returns_original_plaintext_node(self):
        nodes = [
            TextNode(
                "This is plain text",
                TextType.PLAINTEXT
            )
        ]

        expected = [
            TextNode(
                "This is plain text",
                TextType.PLAINTEXT
            )
        ]

        self.assertEqual(
            split_nodes_links(nodes),
            expected
        )

    def test_link_node_preserves_non_plaintext_nodes(self):
        nodes = [
            TextNode(
                "Already bold",
                TextType.BOLD
            )
        ]

        self.assertEqual(
            split_nodes_links(nodes),
            nodes
        )

    def test_multiple_identical_links_split_correctly(self):
        nodes = [
            TextNode(
                "First [link](https://example.com)"
                " and second [link](https://example.com)",
                TextType.PLAINTEXT
            )
        ]

        expected = [
            TextNode(
                "First ",
                TextType.PLAINTEXT
            ),
            TextNode(
                "link",
                TextType.LINK,
                "https://example.com"
            ),
            TextNode(
                " and second ",
                TextType.PLAINTEXT
            ),
            TextNode(
                "link",
                TextType.LINK,
                "https://example.com"
            ),
        ]

        self.assertEqual(
            split_nodes_links(nodes),
            expected
        )