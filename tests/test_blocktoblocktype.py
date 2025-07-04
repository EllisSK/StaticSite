import unittest
from src.nodes import BlockType
from src.functions import block_to_block_type

class TestBlockToBlockType(unittest.TestCase):
    def test_paragraph(self):
        block = "This is just some stupid sample text.\nWoah, newline!"
        expected = BlockType.PARAGRAPH
        result = block_to_block_type(block)
        self.assertEqual(expected, result)

    def test_heading(self):
        block = "### This is a heading"
        expected = BlockType.HEADING
        result = block_to_block_type(block)
        self.assertEqual(expected, result)

    def test_code(self):
        block = "```import pandas```"
        expected = BlockType.CODE
        result = block_to_block_type(block)
        self.assertEqual(expected, result)

    def test_quote(self):
        block = ">Quote 1: Hello\n>Quote 2: Goodbye"
        expected = BlockType.QUOTE
        result = block_to_block_type(block)
        self.assertEqual(expected, result)

    def test_unordered_list(self):
        block = "-Item 1\n-Item 2"
        expected = BlockType.UNORDERED_LIST
        result = block_to_block_type(block)
        self.assertEqual(expected, result)

    def test_ordered_list(self):
        block = "1. Item 1\n2. Item 2\n3. Item 3"
        expected = BlockType.ORDERED_LIST
        result = block_to_block_type(block)
        self.assertEqual(expected, result)
