import unittest
from src.nodes.htmlnode import HTMLNode

'''
    Test cases for HTMLNode
    - init
        - tag (none or tag)
        - value (none or value)
        - children (none or children)
        - props (none or props)
    - props_to_html
        - contains many props
        - contains one prop
    - to_html
        - 
    - repr
        - contains tags
        - contains value
        - contains children
        - contains props
'''

class TestHTMLNode(unittest.TestCase):
    # --- init ---
    def test_tag_assigned_properly(self):
        node = HTMLNode(tag = "this is a tag")
        self.assertEqual("this is a tag", node.tag)

    def test_default_tag_is_none(self):
        node = HTMLNode()
        self.assertIsNone(node.tag)

    def test_value_assigned_properly(self):
        node = HTMLNode(value = "This is a value")
        self.assertEqual("This is a value", node.value)

    def test_default_value_is_none(self):
        node = HTMLNode()
        self.assertIsNone(node.value)

    def test_children_assigned_properly(self):
        child = HTMLNode(tag="this is a tag")
        node = HTMLNode(children=[child])
        self.assertEqual(node.children, [child])

    def test_default_children_is_none(self):
        node = HTMLNode()
        self.assertIsNone(node.children)

    def test_props_assigned_properly(self):
        props = {"href": "https://google.com", "target": "_blank"}
        node = HTMLNode(props=props)
        self.assertEqual(node.props, props)

    def test_default_props_is_none(self):
        node = HTMLNode()
        self.assertIsNone(node.props)

    # --- to_html ---

    # --- props_to_html ---
    def test_props_to_html_sets_single_prop(self):
        node = HTMLNode(props = {"href": "https://google.com"})
        props = node.props_to_html()
        self.assertIn("https://google.com", props)

    def test_props_to_html_sets_multiple_props(self):
        node = HTMLNode(props = {"href": "https://google.com", "target": "_blank"})
        props = node.props_to_html()
        self.assertIn("https://google.com", props)
        self.assertIn("_blank", props)

    # --- repr ---
    def test_repr_contains_tag_when_not_none(self):
        node = HTMLNode(tag = "this is a tag")
        self.assertIn("this is a tag", repr(node))

    def test_repr_contains_value_when_not_none(self):
        node = HTMLNode(value = "this is a value")
        self.assertIn("this is a value", repr(node))

    def test_repr_contains_children_when_not_none(self):
        node = HTMLNode(children = [HTMLNode(tag = "this is a tag")])
        self.assertIn("children:", repr(node))
        self.assertIn("this is a tag", repr(node))

    def test_repr_contains_props_when_not_none(self):
        node = HTMLNode(props = {"href": "https://google.com", "target": "_blank"})
        self.assertIn("props:", repr(node))
        self.assertIn("href", repr(node))
        self.assertIn("https://google.com", repr(node))
        self.assertIn("target", repr(node))