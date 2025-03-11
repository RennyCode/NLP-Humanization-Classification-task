"""
Punctuation Spacing Rule

Purpose:  
Correct punctuation spacing—ensuring no spaces before punctuation and appropriate spaces after punctuation—to reflect proper human typing patterns.

Examples:  
- Example 1:  
  Input: "hello ," (incorrect space before comma)  
  Output: "hello,"
- Example 2:  
  Input: "What's up?Something new" (missing space after question mark)  
  Output: "What's up? Something new"
- Example 3:  
  Input: "Wow!And then" (missing space after exclamation)  
  Output: "Wow! And then"
"""

import re
from rules.utils import clamp

def fix_punctuation_spacing(text):
    """
    Fix punctuation spacing by removing spaces before punctuation and adding spaces after.
    
    Args:
        text (str): The text to modify
        
    Returns:
        str: Modified text with proper punctuation spacing
    """
    # Remove spaces before punctuation
    text = re.sub(r"\s+([,\.!?])", r"\1", text)
    # Ensure there is a space after punctuation if not already present
    text = re.sub(r"([,\.!?])([^\s\d])", r"\1 \2", text)
    return text

def score_punctuation_spacing(text):
    """
    Score the text based on punctuation spacing errors.
    
    Args:
        text (str): The text to score
        
    Returns:
        float: Score between 0 and 1
    """
    missing_spaces = len(re.findall(r'[,\.!?][^\s\d]', text))
    extra_spaces = len(re.findall(r'\s+[,\.!?]', text))
    total_punctuations = len(re.findall(r'[,\.!?]', text))
    
    if total_punctuations == 0:
        return 0
        
    score = (missing_spaces + extra_spaces) / total_punctuations
    return clamp(score) 