import unittest
from block_functions import markdown_to_blocks, block_to_block_type, BlockType


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