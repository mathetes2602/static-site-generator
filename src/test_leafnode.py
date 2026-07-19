import unittest
from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_to_html_a(self):
        node = LeafNode("a", "this is a link", {"href": "google.com"})
        self.assertEqual(node.to_html(), "<a href=\"google.com\">this is a link</a>")

    def test_to_html_p(self):
        node = LeafNode("p", "this is text")
        self.assertEqual(node.to_html(), "<p>this is text</p>")
    
    def test_only_text(self):
        node = LeafNode(value="this is just text")
        self.assertEqual(node.to_html(), "this is just text")