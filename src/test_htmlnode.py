import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_props_eq(self):
        node = HTMLNode(props={"href": "google.com", "target": "blank"})
        correct_string = " href=\"google.com\" target=\"blank\""
        self.assertEqual(node.props_to_html(), correct_string)
    
    def test_props_uneq(self):
        node = HTMLNode(props={"href": "amazon.com", "target": "blank"})
        correct_string = " href=\"google.com\" target=\"blank\""
        self.assertNotEqual(node.props_to_html(), correct_string)

    def test_equal_props(self):
        node = HTMLNode(props={"href": "google.com", "target": "blank"})
        node2 = HTMLNode(props={"href": "google.com", "target": "blank"})  
        self.assertEqual(node.props_to_html(), node2.props_to_html())
