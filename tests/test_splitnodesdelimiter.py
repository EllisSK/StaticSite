import unittest
from src.functions import split_nodes_delimiter
from src.nodes import TextNode, TextType

class TestSplitNodesDelimiter(unittest.TestCase):
    def test_std(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(new_nodes, [TextNode("This is text with a ", TextType.TEXT), TextNode("code block", TextType.CODE), TextNode(" word", TextType.TEXT)])
