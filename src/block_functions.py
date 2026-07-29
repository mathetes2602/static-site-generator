from enum import Enum
import re

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    QUOTE = "quote"
    CODE = "code"
    UNORDERED_LIST = "unordered list"
    ORDERED_LIST = "ordered list"

def markdown_to_blocks(markdown: str):
    split_markdown = markdown.split("\n\n")
    stripped_blocks = []
    for block in split_markdown:
        if block == "":
            continue
        stripped_blocks.append(block.strip())
    return stripped_blocks

def block_to_block_type(block):
    if re.search(r"#{1,6} ", block[0:7]):
        return BlockType.HEADING
    if block[1:5] == "```\n" and block[-4:-1] == "```":
        return BlockType.CODE
    if block[0] == ">":
        return BlockType.QUOTE
    if re.search(r"\n- ", block):
        return BlockType.UNORDERED_LIST
    if re.search(r"\n\d\. ", block):
        return BlockType.ORDERED_LIST

    return BlockType.PARAGRAPH