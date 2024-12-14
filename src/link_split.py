from textnode import TextNode, TextType
import re

def extract_markdown_images(text):
    return (re.findall(r"\!\[(.*?)\]\((.*?)\)", text))

def extract_markdown_links(text):
    return(re.findall(r"\[(.*?)\]\((.*?)\)", text))

def split_nodes_images(old_nodes):
    compiled_list = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            compiled_list.append(node)
            continue
        tempo_list = []
        node_text = re.split(r"(!.*?\))", node.text)
        for piece in range(len(node_text)):
            if node_text[piece] == "":
                continue
            if piece % 2 == 0:
                tempo_list.append(TextNode(node_text[piece], TextType.TEXT))
            else:
                nobj = extract_markdown_images(node_text[piece])[0]
                tempo_list.append(TextNode(nobj[0], TextType.IMAGES, nobj[1]))
        compiled_list.extend(tempo_list)
    return compiled_list

def split_nodes_links(old_nodes):
    compiled_list = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            compiled_list.append(node)
            continue
        tempo_list = []
        node_text = re.split(r"(\[.*?\))", node.text)
        for piece in range(len(node_text)):
            if node_text[piece] == "":
                continue
            if piece % 2 == 0:
                tempo_list.append(TextNode(node_text[piece], TextType.TEXT))
            else:
                nobj = extract_markdown_links(node_text[piece])[0]
                tempo_list.append(TextNode(nobj[0], TextType.LINKS, nobj[1]))
        compiled_list.extend(tempo_list)
    return compiled_list








