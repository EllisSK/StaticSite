import unittest
from parentnode import ParentNode
from leafnode import LeafNode

class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(),
                         "<div><span><b>grandchild</b></span></div>")

    def test_to_html_with_nested_parent(self):
        child_node = LeafNode("b", "child content")
        parent_node2 = ParentNode("h2", [child_node])
        parent_node1 = ParentNode("h1", [parent_node2])
        self.assertEqual(parent_node1.to_html(), 
                         "<h1><h2><b>child content</b></h2></h1>")

    def test_to_html_without_children(self):
        parent_node = ParentNode("h1", [])
        with self.assertRaises(ValueError):
            parent_node.to_html()

    def test_to_html_with_multiple_children(self):
        pass
