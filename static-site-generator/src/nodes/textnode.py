from enum import Enum

from src.nodes.leafnode import LeafNode


class TextType(Enum):
    PLAINTEXT = "plaintext"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGES = "images"

DELIMITERS = {
    TextType.BOLD: "**",
    TextType.ITALIC: "_",
    TextType.CODE: "`",
}

class TextNode:
    def __init__(self,
                 text: str,
                 text_type: TextType,
                 url: str | None = None):
        self.text = text
        self.text_type = text_type
        self.url = url
        self.validate()

    def validate(self):
        # Check types
        if not isinstance(self.text, str):
            raise TypeError(f"text {self} is not of type str")
        if not isinstance(self.text_type, TextType):
            raise TypeError(f"text_type {type(self.text_type)} is not of type TextType")
        if not isinstance(self.url, str | None):
            raise TypeError(f"url {type(self.url)} is not of type str")

        # Check element rules
        if self.text_type == TextType.LINK or self.text_type == TextType.IMAGES:
            if not self.url:
                raise ValueError(f"URL not provided in text_node")

    def __eq__(self, other):
        return (
                self.text == other.text and
                self.text_type == other.text_type and
                self.url == other.url
        )

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"

def text_node_to_html_node(text_node: TextNode) -> LeafNode:
    if not isinstance(text_node, TextNode):
        raise ValueError(f"text_node {text_node} is not of type TextNode")
    match text_node.text_type:
        case TextType.PLAINTEXT:
            return LeafNode(None, text_node.text)
        case TextType.BOLD:
            return LeafNode("b", text_node.text)
        case TextType.ITALIC:
            return LeafNode("i", text_node.text)
        case TextType.CODE:
            return LeafNode("code", text_node.text)
        case TextType.LINK:
            return LeafNode("a", text_node.text, {"href": text_node.url})
        case TextType.IMAGES:
            return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})