import unittest
from extract_link import extract_markdown_links, extract_markdown_images
from link_split import split_nodes_images, split_nodes_links
from main import TextNode, TextType

class regex_test(unittest.TestCase):
    #Here we are testing the scripts to extract the tuples for text and url
    def test1(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        self.assertEqual(extract_markdown_images(text), [('rick roll', 'https://i.imgur.com/aKaOqIh.gif'), ('obi wan', 'https://i.imgur.com/fJRm4Vk.jpeg')])
    def test2(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        self.assertEqual(extract_markdown_links(text), [('to boot dev', 'https://www.boot.dev'), ('to youtube', 'https://www.youtube.com/@bootdotdev')])
    def test3(self):
        self.assertEqual(extract_markdown_links(""), [])
    #Now, were are going to test the functions that we made to generate objects based on the regex for images and links:
    def test4(self):
        nlist =  [TextNode("This is text with a link ", TextType.TEXT),TextNode("to boot dev", TextType.LINKS, "https://www.boot.dev"),TextNode(" and ", TextType.TEXT),TextNode("to youtube", TextType.LINKS, "https://www.youtube.com/@bootdotdev")]
        blist = [TextNode("This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",TextType.TEXT,)]
        self.assertEqual(split_nodes_links(blist), nlist)
    def test5(self):
        self.assertEqual([TextNode("This is just text", TextType.TEXT)], split_nodes_links([TextNode("This is just text", TextType.TEXT)]))
    def test6(self):
        nlist =  [TextNode("This is text with a ", TextType.TEXT),TextNode("rick roll", TextType.IMAGES, "https://i.imgur.com/aKaOqIh.gif"),TextNode(" and ", TextType.TEXT),TextNode("obi wan", TextType.IMAGES, "https://i.imgur.com/fJRm4Vk.jpeg")]
        blist = [TextNode("This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)",TextType.TEXT,)]
        self.assertEqual(split_nodes_images(blist), nlist)
    def test7(self):
        self.assertEqual([TextNode("This is just text", TextType.TEXT)], split_nodes_images([TextNode("This is just text", TextType.TEXT)]))




if __name__ == "__main__":
    unittest.main()