from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag=tag, children=children, props=props)

    def to_html(self):
        if self.tag == None:
            raise ValueError
        if self.children == None:
            raise ValueError("Parent tag with no children")
    
        result = ""
        for child in self.children:
            if child.children:
                result += child.to_html()
            elif child.tag:
                result += f"<{child.tag}{child.props_to_html() or ""}>{child.value or ""}</{child.tag}>"
            else:
                result += child.value
        return f"<{self.tag or ""}{self.props_to_html() or ""}>{result}</{self.tag or ""}>"
    