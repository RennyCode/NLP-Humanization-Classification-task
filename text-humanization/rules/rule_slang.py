"""
Slang Substitution Rule

Purpose:  
Introduce common slang or informal expressions to replace overly formal language, thus enhancing a relaxed, human touch.

Examples:  
- Example 1:  
  Input: "very good"  
  Output: "awesome"
- Example 2:  
  Input: "I am tired"  
  Output: "I'm beat"
- Example 3:  
  Input: "strange"  
  Output: "weird"
"""

import re
from rules.utils import clamp

def fix_slang(text):
    """
    Replace formal expressions with slang or informal expressions.
    
    Args:
        text (str): The text to modify
        
    Returns:
        str: Text with formal expressions replaced by slang
    """
    slang_map = {
        "very good": "awesome",
        "I am tired": "I'm beat",
        "strange": "weird"
    }
    for formal, slang in slang_map.items():
        text = re.sub(r'\b' + formal + r'\b', slang, text, flags=re.IGNORECASE)
    return text

def score_slang(text):
    """
    Score the text based on presence of formal expressions that could be replaced with slang.
    
    Args:
        text (str): The text to score
        
    Returns:
        float: Score between 0 and 1
    """
    slang_map = {
        "very good": "awesome",
        "I am tired": "I'm beat",
        "strange": "weird"
    }
    formal_count = 0
    for phrase in slang_map.keys():
        formal_count += len(re.findall(r'\b' + phrase + r'\b', text, flags=re.IGNORECASE))
    total_words = len(text.split())
    score = formal_count / (total_words + 1)
    return clamp(score) 