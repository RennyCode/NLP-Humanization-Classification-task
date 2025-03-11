import unittest
import random

# Path setup now handled in conftest.py
from rules.rule_capitalization import fix_capitalization, score_capitalization

class TestCapitalizationRule(unittest.TestCase):
    
    def test_capitalization_variation(self):
        """Test that capitalization variations are applied correctly with a fixed seed."""
        # Set a fixed seed for reproducible tests
        random.seed(42)
        
        # Test with fixed seed to get deterministic results
        text = "I went to the store. It was closed."
        transformed = fix_capitalization(text, variation_level=1.0)
        
        # With variation level 1.0, both sentences should be lowercase
        self.assertEqual(transformed, "i went to the store. it was closed.")
        
        # Reset seed and test again for reproducibility
        random.seed(42)
        self.assertEqual(fix_capitalization(text, variation_level=1.0), 
                         "i went to the store. it was closed.")
    
    def test_no_variation(self):
        """Test that no changes are made when variation_level is 0."""
        text = "I went to the store. It was closed."
        self.assertEqual(fix_capitalization(text, variation_level=0), text)
    
    def test_partial_variation(self):
        """Test with a specific seed and partial variation level."""
        random.seed(123)
        text = "First sentence. Second sentence. Third sentence."
        transformed = fix_capitalization(text, variation_level=0.5)
        
        # With seed 123 and variation 0.5, we should see some changes but not all
        # This will depend on the specific seed, so we'll just check it's different
        self.assertNotEqual(transformed, text)
        
        # The text should still contain "sentence" the same number of times
        self.assertEqual(transformed.count("sentence"), text.count("sentence"))
    
    def test_score_perfect_capitalization(self):
        """Test that properly capitalized text gets a score of 0."""
        text = "Hello. This is correct. Another sentence."
        self.assertEqual(score_capitalization(text), 0)
    
    def test_score_imperfect_capitalization(self):
        """Test that improperly capitalized text gets a score > 0."""
        text = "hello. this is incorrect. another sentence."
        self.assertEqual(score_capitalization(text), 1.0)
    
    def test_score_mixed_capitalization(self):
        """Test text with mixed capitalization."""
        text = "Hello. this is mixed. Another sentence."
        expected = 1/3  # 1 out of 3 sentences starts with lowercase
        self.assertEqual(score_capitalization(text), expected)
    
    def test_empty_text(self):
        """Test that empty text is handled correctly."""
        self.assertEqual(fix_capitalization("", variation_level=0.5), "")
        self.assertEqual(score_capitalization(""), 0)

if __name__ == "__main__":
    unittest.main() 