import re
from src.nodes import TextNode, TextType

def split_nodes_image(old_nodes):
    new_nodes = []
    
    for node in old_nodes:
        text = node.text
        links = re.findall(r"!\[(.*?)\]\((.*?)\)", text)

        text_to_split = text
        for alt_text, url in links:
            delimiter = f"![{alt_text}]({url})"
            sections = text_to_split.split(delimiter, 1)

            if sections[0]:
                new_nodes.append(TextNode(sections[0], TextType.TEXT))

            new_nodes.append(TextNode(alt_text, TextType.IMAGE, url))

            text_to_split = sections[1]

        if text_to_split:
            new_nodes.append(TextNode(text_to_split, TextType.TEXT))

    return new_nodes
