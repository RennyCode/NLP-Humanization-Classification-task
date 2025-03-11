"""
Acronym and Abbreviation Rule

Purpose:  
Replace longer phrases with common acronyms/abbreviations (e.g., "by the way" → "btw") to simulate informal, digital communication.

Examples:  
- Example 1:  
  Input: "by the way"  
  Output: "btw"
- Example 2:  
  Input: "for example"  
  Output: "e.g."
- Example 3:  
  Input: "that is"  
  Output: "i.e."
"""

import re
from rules.utils import clamp

def fix_acronyms(text):
    """
    Replace longer phrases with common acronyms/abbreviations.
    
    Args:
        text (str): The text to modify
        
    Returns:
        str: Text with phrases replaced by acronyms/abbreviations
    """
    acronym_map = {
        "by the way": "btw",
        "for example": "e.g.",
        "that is": "i.e."
    }
    for phrase, acronym in acronym_map.items():
        text = re.sub(r'\b' + phrase + r'\b', acronym, text, flags=re.IGNORECASE)
    return text

def score_acronyms(text):
    """
    Score the text based on presence of phrases that could be replaced with acronyms.
    
    Args:
        text (str): The text to score
        
    Returns:
        float: Score between 0 and 1
    """
    acronym_map = {
        "by the way": "btw",
        "for example": "e.g.",
        "that is": "i.e."
    }
    formal_count = 0
    for phrase in acronym_map.keys():
        formal_count += len(re.findall(r'\b' + phrase + r'\b', text, flags=re.IGNORECASE))
    acronym_count = 0
    for acronym in acronym_map.values():
        acronym_count += len(re.findall(re.escape(acronym), text, flags=re.IGNORECASE))
    score = formal_count / (formal_count + acronym_count + 1)
    return clamp(score) 