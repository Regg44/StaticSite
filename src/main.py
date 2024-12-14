from textnode import TextType, TextNode
from htmlnode import HTMLNode, LeafNode, ParentNode
from nodes_delim import split_nodes_delimiter
from link_split import split_nodes_images, split_nodes_links, extract_markdown_images, extract_markdown_links
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















main()