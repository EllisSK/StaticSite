from .htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag: str, children: list, props: dict = None):
        super().__init__(tag=tag, children=children, props=props)

    def to_html(self):
        if not self.tag:
            raise ValueError("ParentNode has no tag")
        if not self.children:
            raise ValueError("ParentNode has no children")
        else:
            return_string = f"<{self.tag}>"
            for node in self.children:
                return_string += node.to_html()
            return_string += f"</{self.tag}>"
            return return_string
