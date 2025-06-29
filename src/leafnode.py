from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag: str, value: str, props: dict = None):
        super().__init__(tag, value, props)

    def to_html(self):
        if not self.value:
            raise ValueError("LeafNode has no value")
        if not self.tag:
            return self.value
        else:
            return f"<{self.tag}>{self.value}</{self.tag}>"
