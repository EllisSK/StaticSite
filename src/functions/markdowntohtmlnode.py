from src.nodes import HTMLNode, TextNode, TextType, BlockType
from src.functions import markdown_to_blocks, text_node_to_html_node, block_to_block_type

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        block_type = block_to_block_type(block)
        match block_type:
            case BlockType.PARAGRAPH:
                text_node = TextNode(block, TextType.TEXT)
            case BlockType.HEADING:
                text_node = TextNode()
            case BlockType.CODE:
                text_node = TextNode()
            case BlockType.QUOTE:
                text_node = TextNode()
            case BlockType.UNORDERED_LIST:
                text_node = TextNode()
            case BlockType.UNORDERED_LIST:
                text_node = TextNode()
        html_node = text_node_to_html_node(text_node)
