from nodes import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    delim_node = False

    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue

        text = old_node.text
        text_list = text.split(delimiter)

        starts_delimitered = False

        if text_list[0] == "":
            text_list.pop(0)
            starts_delimitered = True
        if text_list[-1] == "":
            text_list.pop(-1)

        if starts_delimitered:
            count = 0
        else:
            count = 1

        for string in text_list:
            if count % 2 == 0:
                new_nodes.append(TextNode(string, text_type))
                count += 1
            else:
                new_nodes.append(TextNode(string, TextType.TEXT))
                count += 1

    return new_nodes
