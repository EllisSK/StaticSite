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
        raise NotImplementedError

    def props_to_html(self):
        ret_string = ""
        for item in self.props:
            ret_string += item
            ret_string += "="
            ret_string += '"'
            ret_string += self.props[item]
            ret_string += '" '
        ret_string = ret_string[:-1]
        return ret_string
