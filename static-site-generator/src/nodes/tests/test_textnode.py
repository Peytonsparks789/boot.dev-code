import unittest
from src.nodes.textnode import TextNode, TextType, text_node_to_html_node

'''
    Test cases for TextNode
    - init
        - text
        - text_type
        - url (none or url)
    - validate
        - text is of correct type
        - text_type is of correct type
        - url is of correct type
        - url passed when image or link (not None or "")
    - eq
        - nodes are equal
        - text not equal
        - text_type not equal
        - url not equal
    - repr
        - contains text
        - contains text type
        - contains url
'''

class TestTextNode(unittest.TestCase):
    # --- init ---
    def test_text_assigned_properly(self):
        node = TextNode("...", TextType.BOLD)
        self.assertEqual(node.text, "...")

    def test_text_type_assigned_properly(self):
        for text_type in TextType:
            url = None
            if text_type == TextType.LINK or text_type == TextType.IMAGES:
                url = "https://google.com"
            node = TextNode("...", text_type, url)
            self.assertEqual(node.text_type, text_type)

    def test_url_assigned_properly(self):
        node = TextNode("...", TextType.BOLD, "https://google.com")
        self.assertEqual(node.url, "https://google.com")

    def test_default_url_is_none(self):
        node = TextNode("...", TextType.BOLD)
        self.assertIsNone(node.url)

    # --- validate ---
    def test_validate_text_not_correct_type(self):
        with self.assertRaises(TypeError):
            TextNode(1, TextType.BOLD)

    def test_validate_text_type_not_correct_type(self):
        with self.assertRaises(TypeError):
            TextNode("...", None)

    def test_validate_url_not_correct_type(self):
        with self.assertRaises(TypeError):
            TextNode("...", TextType.LINK, 1)

    def test_validate_error_when_text_type_is_link_and_url_not_provided(self):
        with self.assertRaises(ValueError):
            TextNode("...", TextType.LINK)
        with self.assertRaises(ValueError):
            TextNode("...", TextType.LINK, "")

    def test_validate_error_when_text_type_is_image_and_url_not_provided(self):
        with self.assertRaises(ValueError):
            TextNode("...", TextType.IMAGES)
        with self.assertRaises(ValueError):
            TextNode("...", TextType.IMAGES, "")

    # --- eq ---
    def test_eq(self):
        node = TextNode("...", TextType.BOLD)
        node2 = TextNode("...", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_text_type_not_eq(self):
        node = TextNode("...", TextType.BOLD)
        node2 = TextNode("...", TextType.CODE)
        self.assertNotEqual(node, node2)

    def test_text_not_eq(self):
        node = TextNode("......", TextType.BOLD)
        node2 = TextNode("...", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_url_not_eq(self):
        node = TextNode("...", TextType.BOLD)
        node2 = TextNode("...", TextType.BOLD, "https://google.com")
        self.assertNotEqual(node, node2)

    # --- repr ---
    def test_repr_contains_text(self):
        node = TextNode("...", TextType.BOLD)
        self.assertIn("...", repr(node))

    def test_repr_contains_text_type(self):
        node = TextNode("...", TextType.BOLD)
        self.assertIn("bold", repr(node))

    def test_repr_contains_url(self):
        node = TextNode("...", TextType.BOLD, "https://google.com")
        self.assertIn("https://google.com", repr(node))

'''
Test cases for text_node_to_html_node
- text_node_to_html_node
        - text_node is not an instance of text_node, error
        - plaintext returns text
        - bold returns valid 'b' html node
        - italic returns valid 'i' html node
        - code returns valid "code" html node
        - link returns valid 'a' html node
        - images returns valid "img" html node
'''

class TestTextNodeToHtmlNode(unittest.TestCase):
    def test_text_node_is_not_of_type_text_node_error(self):
        with self.assertRaises(ValueError):
            text_node_to_html_node("test")

    def test_plaintext_returns_string(self):
        node = text_node_to_html_node(TextNode("test", TextType.PLAINTEXT))
        result = node.to_html()
        self.assertEqual(result, "test")

    def test_bold_returns_proper_html_node(self):
        node = text_node_to_html_node(TextNode("test", TextType.BOLD))
        result = node.to_html()
        self.assertEqual(result, "<b>test</b>")

    def test_italic_returns_proper_html_node(self):
        node = text_node_to_html_node(TextNode("test", TextType.ITALIC))
        result = node.to_html()
        self.assertEqual(result, "<i>test</i>")

    def test_code_returns_proper_html_node(self):
        node = text_node_to_html_node(TextNode("test", TextType.CODE))
        result = node.to_html()
        self.assertEqual(result, "<code>test</code>")

    def test_link_returns_proper_html_node(self):
        node = text_node_to_html_node(TextNode("test", TextType.LINK, "https://google.com"))
        result = node.to_html()
        self.assertEqual(result, "<a href=\"https://google.com\">test</a>")

    def test_image_returns_proper_html_node(self):
        node = text_node_to_html_node(TextNode("test", TextType.IMAGES, "https://google.com"))
        result = node.to_html()
        self.assertEqual(result, "<img src=\"https://google.com\" alt=\"test\">")


if __name__ == "__main__":
    unittest.main()