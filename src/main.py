from textnode import TextType, TextNode
from htmlnode import HTMLNode, LeafNode, ParentNode
from nodes_delim import split_nodes_delimiter
from link_split import split_nodes_images, split_nodes_links, extract_markdown_images, extract_markdown_links
from markdown_blocks import BlockType, markdown_to_blocks, block_to_block_type
from src_to_dest import src_to_dest
import os
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
                    split_nodes_delimiter([TextNode(text, TextType.TEXT)], "**", TextType.BOLD), "*", TextType.ITALIC), "`", TextType.CODE
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
            return ParentNode("code", children)
        case BlockType.QUOTE:
            children = []
            for txtnode in text_to_textnodes(block.strip("> ")):
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


def extract_title(markdown):
    lines = markdown.split("\n")
    for line in lines:
        if line.startswith("# "):
            return line.strip("# ")
        continue
    raise Exception("No Header 1 titles in markdown")

def generate_page(from_path, template_path, dest_path):
    print(f"Processing the creationg of page from source {from_path}, to {dest_path}, using {template_path}")
    
    markdown_text = open(from_path, mode='r').read()
    template = open(template_path, mode='r').read()

    HTML_string = markdown_to_html_node(markdown_text).to_html()
    title = extract_title(markdown_text)

    new_html = template.replace("{{ Title }}", title).replace("{{ Content }}", HTML_string)
    print(new_html)
    if not os.path.exists(os.path.dirname(dest_path)):
        os.makedirs(os.path.dirname(dest_path))
    open(dest_path, mode="w").write(new_html)

def generate_pages_recursively(dir_path_content, template_path, dest_dir_path):
    if os.path.isdir(dir_path_content):
        entries = os.listdir(dir_path_content)
    
    for entry in entries:
        entry_path = os.path.join(dir_path_content, entry)
        destin_path = os.path.join(dest_dir_path, entry)
        if entry.endswith(".md"):
            generate_page(entry_path, template_path, destin_path.replace(".md", ".html"))
        elif os.path.isdir(entry_path):
            os.mkdir(destin_path)
            generate_pages_recursively(entry_path, template_path, destin_path)
def initiate():
    src_to_dest("/home/kendall/workspace/github.com/Regg44/StaticSite/static", "/home/kendall/workspace/github.com/Regg44/StaticSite/public")
    generate_pages_recursively("/home/kendall/workspace/github.com/Regg44/StaticSite/content/", "/home/kendall/workspace/github.com/Regg44/StaticSite/template.html", "/home/kendall/workspace/github.com/Regg44/StaticSite/public/")


initiate()
main()