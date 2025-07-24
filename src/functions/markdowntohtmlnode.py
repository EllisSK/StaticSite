from src.nodes import HTMLNode, TextNode, TextType, BlockType
from src.functions import markdown_to_blocks, text_node_to_html_node

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    for block in blocks:

