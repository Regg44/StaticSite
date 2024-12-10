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
            return " ".join(nsentences)
        raise Exception("Invalid format")
    
    #When printed, this will execute and show if no other thing is called.
    def __repr__(self):
        return f"tag={self.tag}, value={self.value}, children={self.children}, props={self.props}"