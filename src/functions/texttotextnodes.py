from nodes import TextType, TextNode
from functions import split_nodes_delimiter, split_nodes_image, split_nodes_link

def text_to_textnodes(text):
    master_node = TextNode(text, TextType.TEXT)
    nodes = [master_node]

    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)

    return nodes

