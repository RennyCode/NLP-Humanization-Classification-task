"""
Verbosity Reduction Rule

Purpose:  
Simplify overly verbose or formal language to a more succinct, conversational form.

Examples:  
- Example 1:  
  Input: "It is my opinion that"  
  Output: "I think"
- Example 2:  
  Input: "Due to the fact that"  
  Output: "Because"
- Example 3:  
  Input: "In the event that"  
  Output: "If"
"""

import re
from rules.utils import clamp

def fix_verbosity(text):
    """
    Simplify overly verbose or formal language.
    
    Args:
        text (str): The text to modify
        
    Returns:
        str: Text with reduced verbosity
    """
    verbosity_map = {
        "It is my opinion that": "I think",
        "Due to the fact that": "Because",
        "In the event that": "If"
    }
    for long_form, short_form in verbosity_map.items():
        text = re.sub(r'\b' + re.escape(long_form) + r'\b', short_form, text, flags=re.IGNORECASE)
    return text

def score_verbosity(text):
    """
    Score the text based on presence of verbose phrases.
    
    Args:
        text (str): The text to score
        
    Returns:
        float: Score between 0 and 1
    """
    verbosity_map = {
        "It is my opinion that": "I think",
        "Due to the fact that": "Because",
        "In the event that": "If"
    }
    long_form_count = 0
    for phrase in verbosity_map.keys():
        long_form_count += len(re.findall(re.escape(phrase), text, flags=re.IGNORECASE))
    total_words = len(text.split())
    score = long_form_count / (total_words + 1)
    return clamp(score) 