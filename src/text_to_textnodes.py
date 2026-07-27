from split_delimiter import split_nodes_delimeter
from split_links import split_nodes_image, split_nodes_link
from textnode import TextType, TextNode

def text_to_textnodes(text):
    start_node = TextNode(text, TextType.TEXT)
    nodes = split_nodes_delimeter([start_node], "**", TextType.BOLD)
    nodes = split_nodes_delimeter(nodes, "_", TextType.ITALIC)
    nodes = split_nodes_delimeter(nodes, "`", TextType.CODE)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    return nodes

