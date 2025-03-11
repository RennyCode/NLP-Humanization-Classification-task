"""
Casual Language Substitution Rule

Purpose:  
Replace overly formal words with more common, casual alternatives to enhance a conversational vibe.

Examples:  
- Example 1:  
  Input: "purchase"  
  Output: "buy"
- Example 2:  
  Input: "assist"  
  Output: "help"
- Example 3:  
  Input: "utilize"  
  Output: "use"
"""

import re
from rules.utils import clamp

def fix_casual_language(text):
    """
    Replace formal words with more casual alternatives.
    
    Args:
        text (str): The text to modify
        
    Returns:
        str: Text with formal words replaced by casual alternatives
    """
    substitution_map = {
        "purchase": "buy",
        "assist": "help",
        "utilize": "use",
        "examine": "check"
    }
    for formal, casual in substitution_map.items():
        text = re.sub(r'\b' + formal + r'\b', casual, text, flags=re.IGNORECASE)
    return text

def score_casual_language(text):
    """
    Score the text based on presence of formal words that could be replaced with casual alternatives.
    
    Args:
        text (str): The text to score
        
    Returns:
        float: Score between 0 and 1
    """
    substitution_map = {
        "purchase": "buy",
        "assist": "help",
        "utilize": "use",
        "examine": "check"
    }
    formal_count = 0
    for formal in substitution_map.keys():
        formal_count += len(re.findall(r'\b' + formal + r'\b', text, flags=re.IGNORECASE))
    total_words = len(text.split())
    score = formal_count / (total_words + 1)
    return clamp(score) 