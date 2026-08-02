import unittest
from block_functions import markdown_to_blocks, block_to_block_type, BlockType, markdown_to_html_node


class TestBlockFuntions(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        md2 = """
This is a single sentence and a new line  

"""
        blocks = markdown_to_blocks(md)
        blocks2 = markdown_to_blocks(md2)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

        self.assertNotEqual(
            blocks,
            "This is some random text"
        )

        self.assertEqual(
            blocks2,
            ["This is a single sentence and a new line"]
        )

    def test_block_to_block_type(self):
        heading_block = "### heading"
        self.assertEqual(
            block_to_block_type(heading_block),
            BlockType.HEADING
        )
        code_block = """
```
This is a code block
```
"""     
        self.assertEqual(
            block_to_block_type(code_block),
            BlockType.CODE
        )

        quote_block = "> This is a quote"
        self.assertEqual(
            block_to_block_type(quote_block),
            BlockType.QUOTE
        )

        ul_block = """
- ul item
- ul item
- ul item
"""     
        self.assertEqual(
            block_to_block_type(ul_block),
            BlockType.UNORDERED_LIST
        )

        ol_block = """"
1. ol item
2. ol item
3. ol item
"""
        self.assertEqual(
            block_to_block_type(ol_block),
            BlockType.ORDERED_LIST
        )

        paragraph_block = "This is just a paragraph"
        self.assertEqual(
            block_to_block_type(paragraph_block),
            BlockType.PARAGRAPH
        )

    def test_paragraph(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p></div>",
        )

    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_lists(self):
        md = """
- This is a list
- with items
- and _more_ items

1. This is an `ordered` list
2. with items
3. and more items

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>This is a list</li><li>with items</li><li>and <i>more</i> items</li></ul><ol><li>This is an <code>ordered</code> list</li><li>with items</li><li>and more items</li></ol></div>",
        )