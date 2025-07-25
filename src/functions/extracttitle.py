def extract_title(markdown):
    """
    Extracts the H1 header from a Markdown string.

    Args:
        markdown: A string containing text in Markdown format.

    Returns:
        The text content of the H1 header, with the leading '#'
        and any surrounding whitespace removed.

    Raises:
        ValueError: If no H1 header is found in the markdown string.
    """
    # Split the markdown content into individual lines
    lines = markdown.split('\n')

    # Iterate through each line to find the H1 header
    for line in lines:
        # Check if the line starts with a single '#' followed by a space,
        # and not '##' which would indicate an H2 header.
        if line.strip().startswith('# '):
            # We found the H1 header.
            # Strip the '#' and any leading/trailing whitespace.
            # The slice `[1:]` removes the first character ('#').
            return line.strip()[1:].strip()

    # If the loop completes without finding an H1 header, raise an exception.
    raise ValueError("No H1 header found in the markdown.")