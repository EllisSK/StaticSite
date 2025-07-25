import re
from ..nodes import HTMLNode, TextNode, TextType, BlockType, LeafNode
from ..functions import markdown_to_blocks, text_node_to_html_node, block_to_block_type, text_to_textnodes

def text_to_children(text):
    """
    Converts a string with inline markdown into a list of HTMLNode objects.
    """
    text_nodes = text_to_textnodes(text)
    children = []
    for text_node in text_nodes:
        children.append(text_node_to_html_node(text_node))
    return children

def heading_to_html_node(block):
    """ Converts a heading block to an HTMLNode. """
    level = 0
    for char in block:
        if char == '#':
            level += 1
        else:
            break
    # Remove the '#' and the space after it
    text_content = block[level:].strip()
    children = text_to_children(text_content)
    return HTMLNode(tag=f"h{level}", children=children)

def code_to_html_node(block):
    """ Converts a code block to an HTMLNode (<pre><code>...). """
    # Remove the ``` fences by splitting the block into lines and taking the content
    lines = block.split("\n")[1:-1]
    
    # Strip leading whitespace from each line to handle indentation
    dedented_lines = [line.lstrip() for line in lines]
    
    # Join the cleaned lines back together and add a final newline, as tests expect
    text_content = "\n".join(dedented_lines) + "\n"
    
    # Create the final <pre><code>...</code></pre> structure
    code_leaf_node = LeafNode(tag="code", value=text_content)
    return HTMLNode(tag="pre", children=[code_leaf_node])

def quote_to_html_node(block):
    """ Converts a quote block to an HTMLNode. """
    lines = block.split('\n')
    # Strip the leading '>' from each line and join them back together
    cleaned_lines = [line.lstrip('>').strip() for line in lines]
    text_content = "\n".join(cleaned_lines)
    children = text_to_children(text_content)
    return HTMLNode(tag="blockquote", children=children)

def ulist_to_html_node(block):
    """ Converts an unordered list block to an HTMLNode (<ul>). """
    items = block.split('\n')
    list_item_nodes = []
    for item in items:
        # Strip the leading '*' or '-' and any whitespace
        text_content = item[1:].strip()
        children = text_to_children(text_content)
        list_item_nodes.append(HTMLNode(tag="li", children=children))
    return HTMLNode(tag="ul", children=list_item_nodes)

def olist_to_html_node(block):
    """ Converts an ordered list block to an HTMLNode (<ol>). """
    items = block.split('\n')
    list_item_nodes = []
    for item in items:
        # Strip the leading number and dot (e.g., "1. ")
        text_content = re.sub(r'^\d+\.\s*', '', item)
        children = text_to_children(text_content)
        list_item_nodes.append(HTMLNode(tag="li", children=children))
    return HTMLNode(tag="ol", children=list_item_nodes)

def paragraph_to_html_node(block):
    """ Converts a paragraph block to an HTMLNode. """
    # Normalize all whitespace (newlines, multiple spaces, etc.)
    # into single spaces between words.
    text_content = " ".join(block.split())
    
    children = text_to_children(text_content)
    return HTMLNode(tag="p", children=children)

def markdown_to_html_node(markdown):
    """
    Converts a full markdown document to a parent HTMLNode.
    """
    blocks = markdown_to_blocks(markdown)
    children_nodes = []

    for block in blocks:
        block_type = block_to_block_type(block)
        
        if block_type == BlockType.HEADING:
            children_nodes.append(heading_to_html_node(block))
        elif block_type == BlockType.CODE:
            children_nodes.append(code_to_html_node(block))
        elif block_type == BlockType.QUOTE:
            children_nodes.append(quote_to_html_node(block))
        elif block_type == BlockType.UNORDERED_LIST:
            children_nodes.append(ulist_to_html_node(block))
        elif block_type == BlockType.ORDERED_LIST:
            children_nodes.append(olist_to_html_node(block))
        else: # Default to PARAGRAPH
            children_nodes.append(paragraph_to_html_node(block))
            
    # Wrap all block nodes in a single parent <div>
    return HTMLNode(tag="div", children=children_nodes)
