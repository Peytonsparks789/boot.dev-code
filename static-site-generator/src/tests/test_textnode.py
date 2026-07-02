import unittest
from src.nodes.textnode import TextNode, TextType

'''
    Test cases for TextNode
    - init
        - text
        - text_type
        - url (none or url)
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
            node = TextNode("...", text_type)
            self.assertEqual(node.text_type, text_type)

    def test_url_assigned_properly(self):
        node = TextNode("...", TextType.BOLD, "https://google.com")
        self.assertEqual(node.url, "https://google.com")

    def test_default_url_is_none(self):
        node = TextNode("...", TextType.BOLD)
        self.assertIsNone(node.url)

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


if __name__ == "__main__":
    unittest.main()