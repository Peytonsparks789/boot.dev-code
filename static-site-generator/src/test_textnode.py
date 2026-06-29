import unittest
from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    def test_text_assigned_properly(self):
        node = TextNode("...", TextType.BOLD)
        self.assertEqual(node.text, "...")

    def test_text_type_assigned_properly(self):
        for text_type in TextType:
            node = TextNode("...", text_type)
            self.assertEqual(node.text_type, text_type)

    def test_url_assigned_properly(self):
        node = TextNode("...", TextType.BOLD, "https://boot.dev")
        self.assertEqual(node.url, "https://boot.dev")

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
        node2 = TextNode("...", TextType.BOLD, "https://boot.dev")
        self.assertNotEqual(node, node2)

    def test_default_url_is_none(self):
        node = TextNode("...", TextType.BOLD)
        self.assertIsNone(node.url)

    def test_repr_contains_text(self):
        node = TextNode("...", TextType.BOLD)
        self.assertIn("...", repr(node))

    def test_repr_contains_text_type(self):
        node = TextNode("...", TextType.BOLD)
        self.assertIn("bold", repr(node))

    def test_repr_contains_url(self):
        node = TextNode("...", TextType.BOLD, "https://boot.dev")
        self.assertIn("https://boot.dev", repr(node))


if __name__ == "__main__":
    unittest.main()