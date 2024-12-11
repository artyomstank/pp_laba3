import unittest
from main import find_hex_colors

class TestHexColorRegex(unittest.TestCase):

    def test_valid_colors(self):
        text = "#fff #123abc #ABC123 #000000"
        expected = ["#fff", "#123abc", "#ABC123", "#000000"]
        self.assertEqual(find_hex_colors(text), expected)

    def test_invalid_colors(self):
        text = "#ff #123abz #GGG123 #12345g"
        expected = []
        self.assertEqual(find_hex_colors(text), expected)

    def test_mixed_text(self):
        text = "Some colors: #fff, invalid: #12345g, valid: #000000 and #123abc."
        expected = ["#fff", "#000000", "#123abc"]
        self.assertEqual(find_hex_colors(text), expected)

    def test_empty_text(self):
        text = ""
        expected = []
        self.assertEqual(find_hex_colors(text), expected)

    def test_no_colors(self):
        text = "This is a text without any hex colors."
        expected = []
        self.assertEqual(find_hex_colors(text), expected)

if __name__ == "__main__":
    unittest.main()
