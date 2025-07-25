from ..nodes import BlockType

def block_to_block_type(block):
    if block[0] == "#":
        return BlockType.HEADING
    elif block[0:3] == "```" and block[-3:] == "```":
        return BlockType.CODE
    
    split_block = block.split("\n")

    starter = split_block[0][0]

    all_same = True
    starters = []
    for line in split_block:
        starters.append(line[:2])
        if line[0] != starter:
            all_same = False

    ordered_check = []
    for n in range(1, len(split_block)+1):
        ordered_check.append(f"{n}.")

    if all_same:
        if starter == ">":
            return BlockType.QUOTE
        elif starter == "-":
            return BlockType.UNORDERED_LIST

    if starters == ordered_check:
        return BlockType.ORDERED_LIST

    return BlockType.PARAGRAPH
