import unittest

from src.markdown_processor.text_to_text_nodes import text_to_text_nodes
from src.nodes.textnode import TextNode, TextType

'''
Test cases for test_text_to_text_nodes.py
- plaintext
- plaintext node remains unchanged
- bold text converted to bold node
- italic text converted to italic node
- code text converted to code node
- image converted to image node
- link converted to link node
- multiple syntax types
- bold, italic, and code processed together
- bold, link, and image processed together
- multiple nodes
- multiple plaintext nodes processed independently
- existing non-plaintext nodes preserved
- multiple occurrences of the same syntax type processed correctly
'''

class TestTextToTextNodes(unittest.TestCase):

    # --- plaintext ---

    def test_plaintext_node_remains_unchanged(self):
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
            text_to_text_nodes(nodes),
            expected
        )

    # --- bold ---

    def test_bold_text_converted_to_bold_node(self):
        nodes = [
            TextNode(
                "This is **bold** text",
                TextType.PLAINTEXT
            )
        ]

        expected = [
            TextNode(
                "This is ",
                TextType.PLAINTEXT
            ),
            TextNode(
                "bold",
                TextType.BOLD
            ),
            TextNode(
                " text",
                TextType.PLAINTEXT
            ),
        ]

        self.assertEqual(
            text_to_text_nodes(nodes),
            expected
        )

    # --- italic ---

    def test_italic_text_converted_to_italic_node(self):
        nodes = [
            TextNode(
                "This is _italic_ text",
                TextType.PLAINTEXT
            )
        ]

        expected = [
            TextNode(
                "This is ",
                TextType.PLAINTEXT
            ),
            TextNode(
                "italic",
                TextType.ITALIC
            ),
            TextNode(
                " text",
                TextType.PLAINTEXT
            ),
        ]

        self.assertEqual(
            text_to_text_nodes(nodes),
            expected
        )

    # --- code ---

    def test_code_text_converted_to_code_node(self):
        nodes = [
            TextNode(
                "This is `code` text",
                TextType.PLAINTEXT
            )
        ]

        expected = [
            TextNode(
                "This is ",
                TextType.PLAINTEXT
            ),
            TextNode(
                "code",
                TextType.CODE
            ),
            TextNode(
                " text",
                TextType.PLAINTEXT
            ),
        ]

        self.assertEqual(
            text_to_text_nodes(nodes),
            expected
        )

    # --- image ---

    def test_image_converted_to_image_node(self):
        nodes = [
            TextNode(
                "This is ![an image](https://image.com/image.png)",
                TextType.PLAINTEXT
            )
        ]

        expected = [
            TextNode(
                "This is ",
                TextType.PLAINTEXT
            ),
            TextNode(
                "an image",
                TextType.IMAGES,
                "https://image.com/image.png"
            ),
        ]

        self.assertEqual(
            text_to_text_nodes(nodes),
            expected
        )

    # --- link ---

    def test_link_converted_to_link_node(self):
        nodes = [
            TextNode(
                "Visit [Boot.dev](https://www.boot.dev)",
                TextType.PLAINTEXT
            )
        ]

        expected = [
            TextNode(
                "Visit ",
                TextType.PLAINTEXT
            ),
            TextNode(
                "Boot.dev",
                TextType.LINK,
                "https://www.boot.dev"
            ),
        ]

        self.assertEqual(
            text_to_text_nodes(nodes),
            expected
        )

    # --- multiple syntax types ---

    def test_bold_italic_and_code_processed_together(self):
        nodes = [
            TextNode(
                "This is **bold**, _italic_, and `code`",
                TextType.PLAINTEXT
            )
        ]

        expected = [
            TextNode(
                "This is ",
                TextType.PLAINTEXT
            ),
            TextNode(
                "bold",
                TextType.BOLD
            ),
            TextNode(
                ", ",
                TextType.PLAINTEXT
            ),
            TextNode(
                "italic",
                TextType.ITALIC
            ),
            TextNode(
                ", and ",
                TextType.PLAINTEXT
            ),
            TextNode(
                "code",
                TextType.CODE
            ),
        ]

        self.assertEqual(
            text_to_text_nodes(nodes),
            expected
        )

    def test_bold_link_and_image_processed_together(self):
        nodes = [
            TextNode(
                "This is **bold** with [a link](https://example.com) "
                "and ![an image](https://image.com/image.png)",
                TextType.PLAINTEXT
            )
        ]

        expected = [
            TextNode(
                "This is ",
                TextType.PLAINTEXT
            ),
            TextNode(
                "bold",
                TextType.BOLD
            ),
            TextNode(
                " with ",
                TextType.PLAINTEXT
            ),
            TextNode(
                "a link",
                TextType.LINK,
                "https://example.com"
            ),
            TextNode(
                " and ",
                TextType.PLAINTEXT
            ),
            TextNode(
                "an image",
                TextType.IMAGES,
                "https://image.com/image.png"
            ),
        ]

        self.assertEqual(
            text_to_text_nodes(nodes),
            expected
        )

    # --- multiple nodes ---

    def test_multiple_plaintext_nodes_processed_independently(self):
        nodes = [
            TextNode(
                "This is **bold**",
                TextType.PLAINTEXT
            ),
            TextNode(
                "This is _italic_",
                TextType.PLAINTEXT
            ),
        ]

        expected = [
            TextNode(
                "This is ",
                TextType.PLAINTEXT
            ),
            TextNode(
                "bold",
                TextType.BOLD
            ),
            TextNode(
                "This is ",
                TextType.PLAINTEXT
            ),
            TextNode(
                "italic",
                TextType.ITALIC
            ),
        ]

        self.assertEqual(
            text_to_text_nodes(nodes),
            expected
        )

    # --- existing non-plaintext nodes ---

    def test_existing_non_plaintext_nodes_preserved(self):
        nodes = [
            TextNode(
                "Already bold",
                TextType.BOLD
            ),
            TextNode(
                "This is **new bold**",
                TextType.PLAINTEXT
            ),
        ]

        expected = [
            TextNode(
                "Already bold",
                TextType.BOLD
            ),
            TextNode(
                "This is ",
                TextType.PLAINTEXT
            ),
            TextNode(
                "new bold",
                TextType.BOLD
            ),
        ]

        self.assertEqual(
            text_to_text_nodes(nodes),
            expected
        )

    # --- multiple occurrences ---

    def test_multiple_occurrences_of_same_syntax_type_processed(self):
        nodes = [
            TextNode(
                "**one** and **two** and **three**",
                TextType.PLAINTEXT
            )
        ]

        expected = [
            TextNode(
                "one",
                TextType.BOLD
            ),
            TextNode(
                " and ",
                TextType.PLAINTEXT
            ),
            TextNode(
                "two",
                TextType.BOLD
            ),
            TextNode(
                " and ",
                TextType.PLAINTEXT
            ),
            TextNode(
                "three",
                TextType.BOLD
            ),
        ]

        self.assertEqual(
            text_to_text_nodes(nodes),
            expected
        )