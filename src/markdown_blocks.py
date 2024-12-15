import re
from enum import Enum
# Class that contains the BlockTypes

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    OLIST = "unordered_list"
    ULIST = "ordered_ list"

# This function will grab a greater piece of text and split it into blocks for our code to handle:
def markdown_to_blocks(text):
    split_txt = []
    for line in text.split("\n\n"):
        if line.strip() == "":
            continue
        else:
            split_txt.append(line.strip())
    return split_txt

# This function is to detect the type of each block
def block_to_block_type(block):
    blocks = block.split("\n")
    if block.startswith("#"):
        return BlockType.HEADING
    elif block.startswith("```") and block.endswith("```"):
        return BlockType.CODE
    elif block.startswith(">"):
        for line in blocks:
            if line.startswith(">"):
                continue
            else:
                return BlockType.PARAGRAPH
        return BlockType.QUOTE
    elif block.startswith("* ") or block.startswith("- "):
        list_char = block[:2]
        for line in blocks:
            if line.startswith(list_char):
                continue
            else:
                return BlockType.PARAGRAPH
        return BlockType.ULIST
    elif block.split(".", maxsplit=1)[0].isnumeric():
        numerator = int(block.split(".", maxsplit=1)[0])
        for line in blocks:
            if line.startswith(f"{numerator}."):
                numerator += 1
                continue
            else:
                return BlockType.PARAGRAPH
        return BlockType.OLIST
    else:
        return BlockType.PARAGRAPH
    

case1 = "#this is a heading"
case2 = "```this is code```"
case3 = "* this is a list\n* with several \n* lines"
case4 = "3. This is another list\n4. But instead of unordered\n5. ordered"
case5 = "This should just return text"

print(block_to_block_type(case1))
print(block_to_block_type(case2))
print(block_to_block_type(case3))
print(block_to_block_type(case4))
print(block_to_block_type(case5))
