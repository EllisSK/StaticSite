class HTMLNode:
    def __init__(self, tag: str = None, value: str = None, children: list = None, props: dict = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def __eq__(self, other):
        if self.tag == other.tag and self.value == other.value and self.children == other.children and self.props == other.props:
            return True
        else:
            return False

    def __repr__(self):
        return f"HTMLNode(\nTag: {self.tag}\nValue: {self.value}\nChildren: {self.children}\nProps: {self.props})"

    def to_html(self):
        if self.tag is None:
            raise ValueError("Invalid HTML: Parent node requires a tag")
        if self.children is None:
            raise ValueError("Invalid HTML: Parent node must have children")

        # Conditionally add a space only if props exist
        props_html = self.props_to_html()
        if props_html:
            props_html = " " + props_html
        
        children_html = ""
        for child in self.children:
            children_html += child.to_html()
        
        return f"<{self.tag}{props_html}>{children_html}</{self.tag}>"

    def props_to_html(self):
        # If there are no props, return an empty string
        if not self.props:
            return ""
        
        # Otherwise, build the attribute string
        attributes = []
        for key, val in self.props.items():
            attributes.append(f'{key}="{val}"')
            
        return " ".join(attributes)
