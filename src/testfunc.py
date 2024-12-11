from main import *
from htmlnode import HTMLNode, LeafNode, ParentNode
from textnode import TextNode, TextType

import unittest

class functiontest(unittest.TestCase):
    
    obj = LeafNode("h1", "Heading 1")
    obj2 = LeafNode("p", "This is a paragraph of text")
    obj3 = LeafNode("b", "this is bold")
    obj4 = LeafNode("i", "this is italics")
    obj5 = LeafNode("a", "this is a link", {"href": "https://www.google.com"})
    obj6 = LeafNode("img", "", {"src": "url/of/image.jpg", "alt": "this is an image"})

    def test1(self):
        self.assertEqual(self.obj.to_html(), "<h1>Heading 1</h1>")
    def test2(self):
        self.assertEqual(self.obj2.to_html(), "<p>This is a paragraph of text</p>")
    def test3(self):
        self.assertEqual(self.obj3.to_html(), "<b>this is bold</b>")
    def test4(self):
        self.assertEqual(self.obj4.to_html(), "<i>this is italics</i>")
    def test5(self):
        self.assertEqual(self.obj5.to_html(), '<a href="https://www.google.com">this is a link</a>')
    def test6(self):
        self.assertEqual(self.obj6.to_html(), '<img src="url/of/image.jpg" alt="this is an image">')
    
    # Here we are going to test the previous created function to change TextNodes into LeafNodes.
    # Define TextNode Objects:
    tobj3 = TextNode("this is bold", TextType.BOLD)
    tobj4 = TextNode("this is italics", TextType.ITALIC)
    tobj5 = TextNode("this is a link", TextType.LINKS, "https://www.google.com")
    tobj6 = TextNode("this is an image", TextType.IMAGES, "url/of/image.jpg")

    def test7(self):
        self.assertEqual(text_node_to_html_node(self.tobj3).to_html(), self.obj3.to_html())
    def test8(self):
        self.assertEqual(text_node_to_html_node(self.tobj4).to_html(), self.obj4.to_html())
    def test9(self):
        self.assertEqual(text_node_to_html_node(self.tobj5).to_html(), self.obj5.to_html())
    def test10(self):
        self.assertEqual(text_node_to_html_node(self.tobj6).to_html(), self.obj6.to_html())




if __name__ == "__main__":
    unittest.main()