from .htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag: str, value: str, props: dict = None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.tag is None:
            return self.value
        
        # Conditionally add a space only if props exist
        props_html = self.props_to_html()
        if props_html:
            props_html = " " + props_html

        # Handle void elements (like <img>)
        if self.value is None:
             return f"<{self.tag}{props_html}>"
        
        # Handle regular elements
        return f"<{self.tag}{props_html}>{self.value}</{self.tag}>"
