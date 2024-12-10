from htmlnode import *
import unittest

class htmltest(unittest.TestCase):
    def test1(self):
        html1 = HTMLNode(value="#", props={"href": "https://www.google.com", "target": "_blank"}, tag="h1")
        self.assertEqual("tag=h1, value=#, children=None, props={'href': 'https://www.google.com', 'target': '_blank'}", str(html1))
    def test2(self):
        html1 = HTMLNode()
        self.assertEqual("tag=None, value=None, children=None, props=None", str(html1))



if __name__ == "__main__":
    unittest.main()