import re

def markdown_to_blocks(markdown):
    """
    Splits a raw Markdown string into a list of blocks.

    Args:
        markdown: A string containing the full Markdown document.

    Returns:
        A list of strings, where each string is a block of Markdown.
    """
    # Split the document by one or more blank lines (lines with optional whitespace).
    # A blank line is represented by '\n\s*\n'.
    # The re.split looks for one or more newlines, capturing the essence of "blank lines".
    split_blocks = re.split(r'\n\s*\n', markdown)
    
    # Filter out any empty strings that may result from the split
    # and strip leading/trailing whitespace from each block.
    cleaned_blocks = [block.strip() for block in split_blocks if block.strip()]
    
    return cleaned_blocks
