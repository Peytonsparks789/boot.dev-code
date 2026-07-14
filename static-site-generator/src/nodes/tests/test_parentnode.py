import unittest

from src.nodes.leafnode import LeafNode
from src.nodes.parentnode import ParentNode

"""
    Test cases for ParentNode
    - to_html
        - raises when tag is None
        - raises when children is None
        - raises when children is empty
        - renders without props
        - renders with one prop
        - renders with multiple props
        - renders multiple LeafNode children
        - renders nested ParentNodes
        - renders deeply nested ParentNodes
        - renders props with nested children
"""

class ParentNodeTest(unittest.TestCase):
    def test_to_html_raise_when_tag_is_none(self):
        parent_node = ParentNode(tag = None, children = ["test"])
        with self.assertRaises(ValueError):
            parent_node.to_html()

    def test_to_html_raise_when_tag_is_empty(self):
        parent_node = ParentNode(tag="", children=["test"])
        with self.assertRaises(ValueError):
            parent_node.to_html()

    def test_to_html_raise_when_children_are_none(self):
        parent_node = ParentNode(tag="p", children=None)
        with self.assertRaises(ValueError):
            parent_node.to_html()

    def test_to_html_raise_when_children_are_empty(self):
        parent_node = ParentNode(tag="p", children=[])
        with self.assertRaises(ValueError):
            parent_node.to_html()

    def test_to_html_renders_properly_when_no_props_present(self):
        expected = "<p><span>child</span></p>"
        child_node = LeafNode(tag = "span", value = "child")
        parent_node = ParentNode(tag="p", children=[child_node], props=None)
        self.assertEqual(parent_node.to_html(), expected)

    def test_to_html_renders_properly_with_one_prop(self):
        expected = "<p target=\"_blank\"><span>child</span></p>"
        child_node = LeafNode(tag = "span", value = "child")
        parent_node = ParentNode(tag="p", children=[child_node], props={"target": "_blank"})
        self.assertEqual(parent_node.to_html(), expected)

    def test_to_html_renders_properly_with_many_props(self):
        expected = "<p href=\"https://google.com\" target=\"_blank\"><span>child</span></p>"
        child_node = LeafNode(tag = "span", value = "child")
        parent_node = ParentNode(tag="p", children=[child_node], props={"href": "https://google.com", "target": "_blank"})
        self.assertEqual(parent_node.to_html(), expected)

    def test_to_html_renders_nested_parent_node(self):
        expected = "<section><div><span>child</span></div></section>"
        child_node = LeafNode(tag="span", value="child")
        inner_parent_node = ParentNode(tag="div", children=[child_node])
        outer_parent_node = ParentNode(tag="section", children=[inner_parent_node])
        self.assertEqual(outer_parent_node.to_html(), expected)

    def test_to_html_renders_deeply_nested_parent_nodes(self):
        expected = "<section><article><div><span>child</span></div></article></section>"
        child_node = LeafNode(tag="span", value="child")
        inner_parent_node = ParentNode(tag="div", children=[child_node])
        middle_parent_node = ParentNode(tag="article", children=[inner_parent_node])
        outer_parent_node = ParentNode(tag="section", children=[middle_parent_node])
        self.assertEqual(outer_parent_node.to_html(), expected)

    def test_to_html_renders_props_with_nested_children(self):
        expected = "<section class=\"container\"><div><span>child</span></div></section>"
        child_node = LeafNode(tag="span", value="child")
        inner_parent_node = ParentNode(tag="div", children=[child_node])
        outer_parent_node = ParentNode(tag="section", children=[inner_parent_node], props={"class": "container"})
        self.assertEqual(outer_parent_node.to_html(), expected)

    def test_to_html_renders_multiple_leaf_node_children(self):
        expected = "<p><span>Hello</span><b>World</b></p>"
        child_node_1 = LeafNode(tag="span", value="Hello")
        child_node_2 = LeafNode(tag="b", value="World")
        parent_node = ParentNode(tag="p", children=[child_node_1, child_node_2])
        self.assertEqual(parent_node.to_html(), expected)