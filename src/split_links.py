from textnode import TextNode, TextType
from link_extractors import extract_markdown_images, extract_markdown_links

def split_nodes_image(old_nodes: list[TextNode]) -> list[TextNode]:
    new_nodes = []
    for node in old_nodes:
        extracted_images = extract_markdown_images(node.text)
        if extracted_images == None:
            new_nodes.append(node)

        nodes = []
        text = node.text
        for image in extracted_images:
            sections = text.split(f"![{image[0]}]({image[1]})", 1)
            if sections[0] != "":
                nodes.append(TextNode(sections[0], TextType.TEXT))
            nodes.append(TextNode(image[0], TextType.IMAGE, image[1]))

            text = None
            if sections[1] and sections[1] != "":
                text = sections[1]
        if text != None:
            nodes.append(TextNode(text, TextType.TEXT))
        new_nodes.extend(nodes)

    return new_nodes

def split_nodes_link(old_nodes: list[TextNode]) -> list[TextNode]:
    new_nodes = []
    for node in old_nodes:
        extracted_images = extract_markdown_links(node.text)
        if extracted_images == None:
            new_nodes.append(node)

        nodes = []
        text = node.text
        for link in extracted_images:
            sections = text.split(f"[{link[0]}]({link[1]})", 1)
            if sections[0] != "":
                nodes.append(TextNode(sections[0], TextType.TEXT))
            nodes.append(TextNode(link[0], TextType.LINK, link[1]))

            text = None
            if sections[1] and sections[1] != "":
                text = sections[1]
        if text != None:
            nodes.append(TextNode(text, TextType.TEXT))
        new_nodes.extend(nodes)

    return new_nodes