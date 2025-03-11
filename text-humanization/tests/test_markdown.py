import unittest
import sys
import os

# Add the parent directory to the path so we can import the rules package
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from rules.rule_markdown import fix_remove_markdown, score_remove_markdown

class TestMarkdownRule(unittest.TestCase):
    
    def test_remove_bold(self):
        """Test removal of bold markdown formatting."""
        test_cases = [
            ("This is **bold** text.", "This is bold text."),
            ("**Bold** at the beginning", "Bold at the beginning"),
            ("At the end **bold**", "At the end bold"),
            ("This has **multiple** bold **sections**", "This has multiple bold sections")
        ]
        
        for input_text, expected in test_cases:
            self.assertEqual(fix_remove_markdown(input_text), expected)
    
    def test_remove_italics(self):
        """Test removal of italic markdown formatting."""
        test_cases = [
            ("This is *italic* text.", "This is italic text."),
            ("*Italic* at the beginning", "Italic at the beginning"),
            ("At the end *italic*", "At the end italic"),
            ("This has *multiple* italic *sections*", "This has multiple italic sections")
        ]
        
        for input_text, expected in test_cases:
            self.assertEqual(fix_remove_markdown(input_text), expected)
    
    def test_remove_links(self):
        """Test removal of markdown links."""
        test_cases = [
            ("Visit [this link](http://example.com)", "Visit this link"),
            ("Multiple [links](http://example1.com) in [text](http://example2.com)",
             "Multiple links in text"),
            ("[Link](http://example.com) at beginning", "Link at beginning"),
            ("At the end [link](http://example.com)", "At the end link")
        ]
        
        for input_text, expected in test_cases:
            self.assertEqual(fix_remove_markdown(input_text), expected)
    
    def test_remove_headers(self):
        """Test removal of markdown headers."""
        test_cases = [
            ("# Heading 1", "Heading 1"),
            ("## Heading 2", "Heading 2"),
            ("### Heading 3", "Heading 3"),
            ("#### Heading 4", "Heading 4"),
            ("##### Heading 5", "Heading 5"),
            ("###### Heading 6", "Heading 6"),
            ("   # Heading with spaces", "Heading with spaces")
        ]
        
        for input_text, expected in test_cases:
            self.assertEqual(fix_remove_markdown(input_text), expected)
    
    def test_combined_markdown(self):
        """Test removal of multiple markdown elements."""
        test_cases = [
            ("# **Bold Header** with *italics*", "Bold Header with italics"),
            ("**Bold** and *italic* and [link](http://example.com)",
             "Bold and italic and link"),
            ("# Heading\n**Bold paragraph** with [a link](http://example.com).",
             "Heading\nBold paragraph with a link.")
        ]
        
        for input_text, expected in test_cases:
            self.assertEqual(fix_remove_markdown(input_text), expected)
    
    def test_no_markdown(self):
        """Test that text without markdown remains unchanged."""
        text = "This text has no markdown formatting."
        self.assertEqual(fix_remove_markdown(text), text)
    
    def test_score_with_no_markdown(self):
        """Test that text without markdown gets a score of 0."""
        text = "This text has no markdown formatting."
        self.assertEqual(score_remove_markdown(text), 0)
    
    def test_score_with_markdown(self):
        """Test scoring text with markdown elements."""
        text = "# Heading\nThis text has **bold** and *italic* formatting."
        score = score_remove_markdown(text)
        self.assertGreater(score, 0, "Score should be greater than 0 for text with markdown")
        self.assertLessEqual(score, 1.0, "Score should be less than or equal to 1.0")
    
    def test_empty_text(self):
        """Test that empty text is handled correctly."""
        self.assertEqual(fix_remove_markdown(""), "")
        self.assertEqual(score_remove_markdown(""), 0)

if __name__ == "__main__":
    unittest.main() 