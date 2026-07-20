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
            if child.children != None:
                result += child.to_html()
            else:
                result += f"<{child.tag}>{child.value}</{child.tag}>"
        return f"<{self.tag}{self.props or ""}>{result}</{self.tag}>"
    