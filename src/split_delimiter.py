from textnode import TextNode, TextType
def split_nodes_delimeter(old_nodes: list[TextNode], delimeter: str, text_type: TextType) -> list[TextNode]:
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        if delimeter in old_node.text:
            nodes_text = old_node.text.split(delimeter)
            nodes = []
            if len(nodes_text) % 2 == 0:
                raise Exception("invalid Markdown syntax")
            for text in nodes_text:
                if text[0] == " " or text[-1] == " ":
                    nodes.append(TextNode(text, TextType.TEXT))
                else:
                    nodes.append(TextNode(text, text_type))
            new_nodes.extend(nodes)
        else:
            new_nodes.append(old_node)
    return new_nodes
