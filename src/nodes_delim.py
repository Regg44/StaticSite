from textnode import TextNode, TextType


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    compiled_list = list()
    nodes_to_play = old_nodes.copy()
    def in_nodes(node):
        if node.text_type != TextType.TEXT:
            compiled_list.append(node)
        if node.text.count(delimiter) % 2 != 0:
            raise Exception("A delimiter wasn't closed.")
        node_text = node.text.split(delimiter)
        node_text[::2] = map(lambda x: TextNode(x, TextType.TEXT), node_text[::2])
        node_text[1::2] = map(lambda x: TextNode(x, text_type), node_text[1::2])
        return node_text
    compiled_list.extend(map(in_nodes, nodes_to_play))
    return compiled_list[0]


sobj = TextNode("This is a *bold* test. We are going to use this single object o to **manifest** several smaller objects. or `code examples`", TextType.TEXT)
print(split_nodes_delimiter([sobj], "*", TextType.BOLD))

print(["hi", "lol", "xd"])