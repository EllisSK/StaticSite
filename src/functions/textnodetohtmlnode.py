from nodes import TextType, LeafNode

def text_node_to_html_node(text_node):
    if not isinstance(text_node.text_type, TextType):
        raise Exception("Text node text type is not in TextType")
    
    tag = None
    value = None
    props = None

    if text_node.text_type == TextType.TEXT:
        value = text_node.text
    elif text_node.text_type == TextType.BOLD:
        tag = "b"
        value = text_node.text
    elif text_node.text_type == TextType.ITALIC:
        tag = "i"
        value = text_node.text
    elif text_node.text_type == TextType.CODE:
        tag = "code"
        value = text_node.text
    elif text_node.text_type == TextType.LINK:
        tag = "a"
        props = {}
        props["href"] = text_node.url
    elif text_node.text_type == TextType.IMAGE:
        tag = "img"
        props = {}
        props["src"] = text_node.url
        props["alt"] = text_node.text

    leaf_node = LeafNode(tag, value, props)
    return leaf_node
