from src.htmlnode import HTMLNode


class LeafNode(HTMLNode):
    def __init__(self,
                 value : str,
                 tag : str | None,
                 props : dict | None = None):
        super().__init__(
            value = value,
            tag = tag,
            children = None,
            props = props)

    def to_html(self):
        if not self.value:
            raise ValueError("All leaf nodes must have a value")
        if not self.tag:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

    def __repr__(self):
        return f"tag: {self.tag}, value: {self.value}, props: {self.props}"