import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_none_eq(self):
        node1 = HTMLNode()
        node2 = HTMLNode()
        self.assertEqual(node1, node2)

    def test_to_html(self):
        test_dict = {
    "href": "https://www.google.com",
    "target": "_blank"}
        node = HTMLNode(props=test_dict)
        result = 'href="https://www.google.com" target="_blank"'
        self.assertEqual(node.props_to_html(), result)

    def test_repr(self):
        node = HTMLNode()
        result = "HTMLNode(\nTag: None\nValue: None\nChildren: None\nProps: None)"
        self.assertEqual(repr(node), result)
