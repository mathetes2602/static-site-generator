import unittest
from main import extract_title

class TestMain(unittest.TestCase):
    def test_extract_title(self):
        md = "# Hello"
        self.assertEqual(
            extract_title(md),
            "Hello"
        )

        md2 = '''
Just a line of text
# This is a header
Another line of text
'''     
        self.assertEqual(
            extract_title(md2),
            "This is a header"
        )
