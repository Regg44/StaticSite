from htmlnode import *
import unittest

class htmltest(unittest.TestCase):
    def test1(self):
        html1 = HTMLNode(value="#", props={"href": "https://www.google.com", "target": "_blank"}, tag="h1")
        self.assertEqual("tag=h1, value=#, children=None, props={'href': 'https://www.google.com', 'target': '_blank'}", str(html1))
    def test2(self):
        html1 = HTMLNode()
        self.assertEqual("tag=None, value=None, children=None, props=None", str(html1))

class leaftest(unittest.TestCase):
    def test1(self):
        obj1 = LeafNode("a", "vamo pa la fiesta mi rico", {"href": "www.boot.com"})
        print(obj1.to_html())
        self.assertIsInstance(obj1.to_html(), str) 
    
    def test2(self):
        obj1 = LeafNode("p", "This is an example test to do tests and stuff alike")
        print(obj1.to_html())
        self.assertIsInstance(obj1.to_html(), str)

class parenttest(unittest.TestCase):
    node = ParentNode(
    "p",
    children=[
        LeafNode("b", "Bold text"),
        LeafNode(None, "Normal text"),
        LeafNode("i", "italic text"),
        LeafNode(None, "Normal text"),
    ],
    )

    node2 = ParentNode("h1", children=[node, LeafNode("b", "bald")],)
    print(node.to_html())
    print(node2.to_html())

if __name__ == "__main__":
    unittest.main()