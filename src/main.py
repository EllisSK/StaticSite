from textnode import TextNode, TextType

def main():
    textnode = TextNode("This is a test.", TextType.BOLD, "www.test.com")
    print(repr(textnode))

main()
