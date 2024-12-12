from textnode import TextNode, TextType


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    compiled_list = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            compiled_list.append(node)
            continue
        if node.text.count(delimiter) % 2 != 0:
            raise Exception("A delimiter wasn't closed.")
        tempo_list = []
        node_text = node.text.split(delimiter)
        for piece in range(len(node_text)):
            if piece % 2 == 0:
                tempo_list.append(TextNode(node_text[piece], TextType.TEXT))
            else:
                tempo_list.append(TextNode(node_text[piece], text_type))
        compiled_list.extend(tempo_list)
    return compiled_list



        


sobj = TextNode("This is a *bold* test. We are going to use this single object o to **manifest** several smaller objects. or `code examples`", TextType.TEXT)
print(split_nodes_delimiter([sobj], "*", TextType.BOLD))

print(["hi", "lol", "xd"])