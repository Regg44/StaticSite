from textnode import TextType, TextNode
from htmlnode import HTMLNode, LeafNode, ParentNode
from nodes_delim import split_nodes_delimiter
from link_split import split_nodes_images, split_nodes_links, extract_markdown_images, extract_markdown_links
from markdown_blocks import BlockType, markdown_to_blocks, block_to_block_type
def main():
    obj1 = TextNode("So, we are cooking, or nah...?", TextType.BOLD, "https://www.bootdev.com/")
    print(obj1)


    
def text_node_to_html_node(TextNodeObj):
    match TextNodeObj.text_type:
        case TextType.TEXT:
            obj = LeafNode(value=TextNodeObj.text)
            return obj
        case TextType.BOLD:
            obj = LeafNode(tag="b", value=TextNodeObj.text)
            return obj
        case TextType.ITALIC:
            obj = LeafNode(tag="i", value=TextNodeObj.text)
            return obj
        case TextType.CODE:
            obj = LeafNode(tag="code", value=TextNodeObj.text)
            return obj
        case TextType.LINKS:
            obj = LeafNode(tag="a", value=TextNodeObj.text, props={"href": TextNodeObj.url})
            return obj
        case TextType.IMAGES:
            obj = LeafNode(tag="img", value="", props={"src": TextNodeObj.url, "alt": TextNodeObj.text})
            return obj
        case _:
            raise Exception("TextType invalid.")

def text_to_textnodes(text):
    return split_nodes_links(
        split_nodes_images(
            split_nodes_delimiter(
                split_nodes_delimiter(
                    split_nodes_delimiter([TextNode(text, TextType.TEXT)], "**", TextType.BOLD), "*", TextType.ITALIC), "```", TextType.CODE
                )
            )
        )
def block_to_parentnode(block):
    match block_to_block_type(block):
        case BlockType.PARAGRAPH:
            children = []
            for txtnode in text_to_textnodes(block):
                children.append(text_node_to_html_node(txtnode))
            return ParentNode("p", children)
        case BlockType.HEADING:
            children = []
            heading_n = len(block.split(" ")[0])
            for txtnode in text_to_textnodes(block.strip("#").strip(" ")):
                children.append(text_node_to_html_node(txtnode))
            return ParentNode(f"h{heading_n}", children)
        case BlockType.CODE:
            children = []
            for txtnode in text_to_textnodes(block):
                children.append(text_node_to_html_node(txtnode))
            return ParentNode("```", children)
        case BlockType.QUOTE:
            children = []
            for txtnode in text_to_textnodes(block):
                children.append(text_node_to_html_node(txtnode))
            return ParentNode("blockquote", children)
        case BlockType.ULIST:
            subparent = []
            lines = block.split("\n")
            for line in lines:
                clear_line = line.split(" ", maxsplit=1)[1]
                subparent.append(ParentNode("li", list(map(text_node_to_html_node, text_to_textnodes(clear_line)))))
            return ParentNode("ul", subparent)
        case BlockType.OLIST:
            subparent = []
            lines = block.split("\n")
            for line in lines:
                clear_line = line.split(" ", maxsplit=1)[1]
                subparent.append(ParentNode("li", list(map(text_node_to_html_node, text_to_textnodes(clear_line)))))
            return ParentNode("ol", subparent)
        case _:
            raise Exception("invalid block type")
        

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    page = []
    for block in blocks:
        page.append(block_to_parentnode(block))
    return ParentNode("html", page)

text = (""" ### This is a heading

This is a paragraph of text. It has some **bold** and *italic* words inside of it.

* Now what should this be?
* Unordered list that is
* Now what in the actual hell?

1. Now this is ordered
2. so it should print like so""")
                
print(markdown_to_html_node(text).to_html())
    

main()