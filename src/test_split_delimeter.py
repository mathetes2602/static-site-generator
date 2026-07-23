import unittest
from split_delimiter import split_nodes_delimeter
from textnode import TextNode, TextType

class TestSplitDelimeter(unittest.TestCase):
    def test_code_block(self):
        node = TextNode("This is a text with `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimeter([node], "`", TextType.CODE)
        self.assertEqual(
            new_nodes,
            [
                TextNode("This is a text with ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" word", TextType.TEXT)
                ]
        )
    
    def test_bold_text(self):
        node = TextNode("This is a text with **bold** word", TextType.TEXT)
        new_nodes = split_nodes_delimeter([node], "**", TextType.BOLD)
        self.assertEqual(
            new_nodes,
            [
                TextNode("This is a text with ", TextType.TEXT),
                TextNode("bold", TextType.BOLD),
                TextNode(" word", TextType.TEXT)
                ]
        )
