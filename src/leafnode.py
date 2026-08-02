from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag=None, value=None, props=None):
        super().__init__(tag=tag, value=value, props=props)
    
    def to_html(self):
        if self.value == None:
            raise ValueError
        if self.tag == None:
            return self.value
        return f"<{self.tag or ""}{self.props_to_html() or ""}>{self.value}</{self.tag or ""}>"

    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"