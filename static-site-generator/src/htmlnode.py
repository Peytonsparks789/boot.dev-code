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
        val = ""
        if self.props:
            for key, value in self.props.items():
                val += f" {key}={value}"
        return val.strip()

    def __repr__(self):
        return f"tag: {self.tag}, value: {self.value}, children: {self.children}, props: {self.props}"