import re
from enum import Enum


class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def markdown_to_blocks(markdown: str):
    blocks = markdown.split("\n\n")
    return [block.strip() for block in blocks if block.strip()]

def block_to_block_type(block: str):
    match block:
        case block if block.startswith("# "):
            return BlockType.HEADING
        case block if block.startswith("```"):
            return BlockType.CODE
        case block if block.startswith(">"):
            return BlockType.QUOTE
        case block if block.startswith("-"):
            return BlockType.UNORDERED_LIST
        case block if all(re.match(r"^\d+\. ", line) for line in block.split("\n")):
            return BlockType.ORDERED_LIST
        case _:
            return BlockType.PARAGRAPH