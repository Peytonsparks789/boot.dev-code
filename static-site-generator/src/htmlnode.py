class HTMLNode:
    def __init__(self,
                 tag : str | None = None,
                 value : str | None = None,
                 children : list | None = None,
                 props : dict | None = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        if self.props:
            return f" {" ".join(f"{key.strip()}=\"{value.strip()}\"" for key, value in self.props.items())}"
        return ""

    def __repr__(self):
        return f"tag: {self.tag}, value: {self.value}, children: {self.children}, props: {self.props}"