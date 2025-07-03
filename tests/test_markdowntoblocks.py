import unittest
from src.functions import markdown_to_blocks

class TestMarkdownToBlocks(unittest.TestCase):
    def test_std(self):
        doc = "# This is a heading\n\nThis is a paragraph of text. It has some **bold** and _italic_ words inside of it.\n\n- This is the first list item in a list block\n- This is a list item\n- This is another list item"
        expected = ["# This is a heading", "This is a paragraph of text. It has some **bold** and _italic_ words inside of it.", "- This is the first list item in a list block\n- This is a list item\n- This is another list item"]
        result = markdown_to_blocks(doc)
        self.assertEqual(expected, result)
