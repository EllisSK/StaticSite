import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_repr(self):
        node = TextNode("This is sample text", TextType.ITALIC)
        expected_repr = "TextNode(This is sample text, TextType.ITALIC, None)"
        self.assertEqual(repr(node), expected_repr)

    def test_not_eq(self):
        node1 = TextNode("This is some text", TextType.TEXT)
        node2 = TextNode("This is some different text!", TextType.TEXT)
        self.assertNotEqual(node1, node2)

    def test_eq_url(self):
        node1 = TextNode("T", TextType.LINK, "www.google.com")
        node2 = TextNode("T", TextType.LINK, "www.google.com")

if __name__ == "__main__":
    unittest.main()
