import unittest
from textnode import TextType, TextNode
from text_to_textnodes import text_to_textnodes

class TestTextToTextNode(unittest.TestCase):
    def test_only_bold(self):
        text = "This is a text with **some bold** words"
        nodes = text_to_textnodes(text)
        self.assertEqual(
            nodes,
            [
                TextNode("This is a text with ", TextType.TEXT),
                TextNode("some bold", TextType.BOLD),
                TextNode(" words", TextType.TEXT)
            ]
        )

    def test_bold_italic(self):
        text = "This is a text with **some bold** and _some italic_ words"
        nodes = text_to_textnodes(text)
        self.assertEqual(
            nodes,
            [
                TextNode("This is a text with ", TextType.TEXT),
                TextNode("some bold", TextType.BOLD),
                TextNode(" and ", TextType.TEXT),
                TextNode("some italic", TextType.ITALIC),
                TextNode(" words", TextType.TEXT)
            ]
        )

    def test_all_features(self):
        text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        nodes = text_to_textnodes(text)
        self.assertEqual(
            nodes,
            [
                TextNode("This is ", TextType.TEXT),
                TextNode("text", TextType.BOLD),
                TextNode(" with an ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" word and a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" and an ", TextType.TEXT),
                TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
                TextNode(" and a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://boot.dev"),
            ]
        )
    