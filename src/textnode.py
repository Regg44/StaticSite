from enum import Enum

class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINKS = "links"
    IMAGES = "images"

class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url
    def __eq__(self, textnode2):
        return (
            self.text == textnode2.text and 
            self.text_type == textnode2.text_type and 
            self.url == textnode2.url
        )
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"