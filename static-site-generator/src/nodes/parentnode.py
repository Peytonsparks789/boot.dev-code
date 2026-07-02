from src.nodes.htmlnode import HTMLNode


class ParentNode(HTMLNode):
    def __init__(self,
                 tag: str,
                 children: list,
                 props: dict | None = None):
        super().__init__(
            tag = tag,
            children = children,
            props = props
        )

    def to_html(self):
        if not self.tag:
            raise ValueError("Tag is a required argument for parent nodes")
        if not self.children:
            raise ValueError("Children is a required argument for parent nodes")

        result = f"<{self.tag}{self.props_to_html()}>"
        for child in self.children:
            result += child.to_html()
        return result + f"</{self.tag}>"

    def __repr__(self):
        return f"tag: {self.tag}, children: {self.children}, props: {self.props}"