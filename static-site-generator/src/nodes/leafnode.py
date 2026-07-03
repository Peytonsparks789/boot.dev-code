from src.nodes.htmlnode import HTMLNode

VOID_ELEMENTS = {"img"}


class LeafNode(HTMLNode):
    def __init__(self,
                 tag: str | None,
                 value : str,
                 props : dict | None = None):
        super().__init__(
            tag = tag,
            value = value,
            children = None,
            props = props)

    def to_html(self):
        if self.tag not in VOID_ELEMENTS and not self.value:
            raise ValueError("All non-void leaf nodes must have a value")
        if not self.tag:
            return self.value
        if self.tag in VOID_ELEMENTS:
            return f"<{self.tag}{self.props_to_html()}>"
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

    def __repr__(self):
        return f"tag: {self.tag}, value: {self.value}, props: {self.props}"