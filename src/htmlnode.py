#we are defining the class HTMLNODE for later use here

class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    #To be replaced by children
    def to_html():
        raise NotImplemented
    
    #added tester to see also if .props is valid, if not to raise an exception
    def props_to_html(self):
        if isinstance(self.props, dict):
            nsentences = list(map(lambda x: f'{x}="{self.props[x]}"', self.props))
            return " " + " ".join(nsentences)
        if self.props == None:
            return ""
    
    #When printed, this will execute and show if no other thing is called.
    def __repr__(self):
        return f"tag={self.tag}, value={self.value}, children={self.children}, props={self.props}"

class LeafNode(HTMLNode):
    def __init__(self, tag=None, value=None, props=None):
        super().__init__(tag=tag, value=value, props=props, children=None)
    def to_html(self):
        if self.value == None:
            raise ValueError("All leaf notes must have a value")
        if self.tag == None:
            return self.value
        if self.tag == "img":
            return f"<{self.tag}{self.props_to_html()}>{self.value}"
        else:
            return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
    
class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag=tag, value=None, children=children, props=props)
    def to_html(self):
        if self.tag == None:
            raise ValueError("No tag present, cannot proceed")
        if self.children == None:
            raise ValueError("ParentNode must have children")
        else:
            line_so_far = "".join(list(map(lambda x: x.to_html(), self.children)))
            return f"<{self.tag}{self.props_to_html()}>{line_so_far}</{self.tag}>"

