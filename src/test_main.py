from main import *
import unittest

class main_test(unittest.TestCase):
    def test(self):
        raw_html = """<html><h1>This is a heading</h1><ol><li>Its nice</li><li>To Have</li><li>An ordered <b>list</b></li></ol><p>But don't fret!</p></html>"""
        markdown = """# This is a heading

1. Its nice
2. To Have
3. An ordered **list**

But don't fret!"""
        html = markdown_to_html_node(markdown).to_html()
        self.assertEqual(raw_html, html)
    def test1(self):
        raw_html = """<html><h3>This is a heading</h3><p>This is a paragraph of text. It has some <b>bold</b> and <i>italic</i> words inside of it.</p><ul><li>Now what should this be?</li><li>Unordered list that is</li><li>Now what in the actual hell?</li></ul><ol><li>Now this is ordered</li><li>so it should print like so</li></ol></html>"""
        markdown = """### This is a heading

This is a paragraph of text. It has some **bold** and *italic* words inside of it.

* Now what should this be?
* Unordered list that is
* Now what in the actual hell?

1. Now this is ordered
2. so it should print like so"""
        html = markdown_to_html_node(markdown).to_html()
        print(html)
        self.assertEqual(raw_html, html)
    
    def test2(self):
        markdown = """So this is life
not going to lie, its pretty
pretty as in beauty
that can be the title

# BEAUTY

## SUBTITLE IS BEAUTY AGAIN

# any subsequen title is a minor title h1"""
        self.assertEqual(extract_title(markdown), "BEAUTY")
    

if __name__ == "__main__":
    unittest.main()