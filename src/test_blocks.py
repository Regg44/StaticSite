import unittest
from markdown_blocks import markdown_to_blocks
from markdown_blocks import block_to_block_type



class testblocks(unittest.TestCase):
    def test1(self):
        text = (""" # This is a heading

This is a paragraph of text. It has some **bold** and *italic* words inside of it.

                         


* This is the first list item in a list block
* This is a list item
* This is another list item""")
        comparator = ['# This is a heading', 'This is a paragraph of text. It has some **bold** and *italic* words inside of it.', '* This is the first list item in a list block\n* This is a list item\n* This is another list item']
        self.assertEqual(markdown_to_blocks(text), comparator)
    def test2(self):
        text = ("""This is clearly a text **right**?

Well is not as clear as you might expect
things usually differ between text managers,
but at the end, is something to deal with

end of story


right?





Right????""")
        comparator = ['This is clearly a text **right**?',
                      'Well is not as clear as you might expect\nthings usually differ between text managers,\nbut at the end, is something to deal with',
                      'end of story',
                      'right?',
                      'Right????']
        self.assertEqual(markdown_to_blocks(text), comparator)
    def test3(self):
        text = ("""This is a test but to see edge cases
like the text not having really any separation at all
it should return one block, no more""")
        comparator = ['This is a test but to see edge cases\nlike the text not having really any separation at all\nit should return one block, no more']
        self.assertEqual(markdown_to_blocks(text), comparator)
    def test4(self):
        case1 = "#this is a heading"
        self.assertEqual(block_to_block_type(case1), "heading")
    def test5(self):
        case2 = "```this is code```"
        self.assertEqual(block_to_block_type(case2), "code")
    def test6(self):
        case3 = "* this is a list\n* with several \n* lines"
        self.assertEqual(block_to_block_type(case3), "unordered_list")
    def test7(self):
        case4 = "3. This is another list\n4. But instead of unordered\n5. ordered"
        self.assertEqual(block_to_block_type(case4), "ordered_list")
    def test8(self):
        case5 = "This should just return text"
        self.assertEqual(block_to_block_type(case5), "paragraph")
    def test9(self):
        item = ("* This should also return a paragraph\n- As the delimiters are different\n* for the start of the lines","paragraph")
        self.assertEqual(block_to_block_type(item[0]), item[1])
    def test10(self):
        item = ("7. This should return\n9. A paragraph aswell","paragraph")
        self.assertEqual(block_to_block_type(item[0]), item[1])
    def test11(self):
        item = ("12. This should return\n13. ordered list though","ordered_list")
        self.assertEqual(block_to_block_type(item[0]), item[1])
    
        
        



if __name__ == "__main__":
    unittest.main()