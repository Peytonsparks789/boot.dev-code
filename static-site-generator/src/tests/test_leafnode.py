import unittest
from src.leafnode import LeafNode

'''
    Test cases for LeafNode
    - to_html
        - props is None
        - props is ""
        - single prop
        - many props
        - error on None or "" value
        - tag present wraps value
        - tag not present does not wrap value
    - repr
        - contains tags
        - contains value
        - contains props
'''

class TestLeafNode(unittest.TestCase):
    # --- to_html ---
    def test_to_html_prop_not_rendered_when_prop_is_none(self):
        node = LeafNode(
            value = "Hello, world!",
            tag = "p")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_to_html_prop_not_rendered_when_prop_is_empty(self):
        node = LeafNode(
            value = "Hello, world!",
            tag = "p",
            props = {} )
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_to_html_single_prop_rendered_when_only_one_prop_present(self):
        node = LeafNode(
            value = "Hello, world!",
            tag = "p",
            props = {"href": "https://google.com"})
        self.assertEqual(node.to_html(), "<p href=\"https://google.com\">Hello, world!</p>")

    def test_to_html_many_props_rendered_when_many_props_present(self):
        node = LeafNode(
            value = "Hello, world!",
            tag = "p",
            props = {"href": "https://google.com", "target": "_blank"})
        self.assertEqual(node.to_html(), "<p href=\"https://google.com\" target=\"_blank\">Hello, world!</p>")

    def test_to_html_value_equals_none_throws_error(self):
        node = LeafNode(
            value = None,
            tag = "p",
        )
        with self.assertRaises(ValueError):
            node.to_html()

    def test_to_html_value_equals_blank_throws_error(self):
        node = LeafNode(
            value = "",
            tag = "p"
        )
        with self.assertRaises(ValueError):
            node.to_html()

    def test_to_html_tag_equals_none_returns_value(self):
        node = LeafNode(
            value = "Hello, world!",
            tag = None
        )
        self.assertEqual(node.to_html(), "Hello, world!")

    def test_to_html_tag_equals_blank_returns_value(self):
        node = LeafNode(
            value = "Hello, world!",
            tag = ""
        )
        self.assertEqual(node.to_html(), "Hello, world!")

    def test_to_html_tag_present_wraps_value(self):
        node = LeafNode(
            value = "Hello, world!",
            tag = "p",
        )
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    # --- repr ---
    def test_repr_contains_tag_when_not_none(self):
        node = LeafNode(
            value = "this is a value",
            tag = "this is a tag")
        self.assertIn("this is a tag", repr(node))

    def test_repr_contains_value_when_not_none(self):
        node = LeafNode(
            value = "this is a value",
            tag = None)
        self.assertIn("this is a value", repr(node))

    def test_repr_contains_props_when_not_none(self):
        node = LeafNode(
            value = "this is a value",
            tag = "p",
            props = {"href": "https://google.com", "target": "_blank"})
        self.assertIn("props:", repr(node))
        self.assertIn("href", repr(node))
        self.assertIn("https://google.com", repr(node))
        self.assertIn("target", repr(node))