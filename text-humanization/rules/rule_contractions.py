"""
Contraction Usage Rule

Purpose:  
Convert formal expressions into contractions (e.g., "do not" → "don't") to create a friendlier, more casual tone.

Examples:  
- Example 1:  
  Input: "do not"  
  Output: "don't"
- Example 2:  
  Input: "cannot"  
  Output: "can't"
- Example 3:  
  Input: "I am"  
  Output: "I'm"
"""

import re
from rules.utils import clamp

def fix_contractions(text):
    """
    Convert formal expressions into contractions.
    
    Args:
        text (str): The text to modify
        
    Returns:
        str: Text with formal expressions converted to contractions
    """
    contraction_map = {
        "do not": "don't",
        "cannot": "can't",
        "I am": "I'm",
        "will not": "won't",
        "is not": "isn't"
    }
    for formal, contraction in contraction_map.items():
        text = re.sub(r'\b' + formal + r'\b', contraction, text, flags=re.IGNORECASE)
    return text

def score_contractions(text):
    """
    Score the text based on presence of formal expressions that could be contractions.
    
    Args:
        text (str): The text to score
        
    Returns:
        float: Score between 0 and 1
    """
    contraction_map = {
        "do not": "don't",
        "cannot": "can't",
        "I am": "I'm",
        "will not": "won't",
        "is not": "isn't"
    }
    formal_count = 0
    for formal in contraction_map.keys():
        formal_count += len(re.findall(r'\b' + formal + r'\b', text, flags=re.IGNORECASE))
    total_words = len(text.split())
    score = formal_count / (total_words + 1)
    return clamp(score) 