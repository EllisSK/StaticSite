from nodes import TextNode, TextType
from functions import copy_static

def main():
    copy_static()
    textnode = TextNode("This is a test.", TextType.BOLD, "www.test.com")
    print(repr(textnode))

main()