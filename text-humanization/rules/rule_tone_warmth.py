"""
Tone Warmth Adjustment Rule

Purpose:  
Modify the overall tone to be warmer and more empathetic by adding friendly phrases and softening direct language.

Examples:  
- Example 1:  
  Input: "The solution is provided."  
  Output: "I hope, the solution is provided."
- Example 2:  
  Input: "The error occurred."  
  Output: "Oops, the error occurred."
- Example 3:  
  Input: "Invalid input."  
  Output: "Hmm, invalid input."
"""

import random
import re
from rules.utils import clamp, split_sentences

def fix_tone_warmth(text, warmth_level=0.2):
    """
    Adjust the tone to be warmer and more empathetic.
    
    Args:
        text (str): The text to modify
        warmth_level (float): Probability of adding a warm phrase
        
    Returns:
        str: Text with warmer tone
    """
    # Don't add friendly prefixes if they already exist
    friendly_prefixes = ["I hope", "Oops", "Hmm"]
    if any(prefix.lower() in text.lower() for prefix in friendly_prefixes):
        return text
        
    sentences = split_sentences(text)
    
    # Apply to at most one sentence
    if not sentences or random.random() >= warmth_level:
        return text
        
    sentence_idx = random.randint(0, len(sentences) - 1)
    if sentences[sentence_idx]:
        sentences[sentence_idx] = random.choice(friendly_prefixes) + ", " + sentences[sentence_idx]
    
    return " ".join(sentences)

def score_tone_warmth(text):
    """
    Score the text based on presence of warm phrases.
    
    Args:
        text (str): The text to score
        
    Returns:
        float: Score between 0 and 1
    """
    friendly_prefixes = ["I hope", "Oops", "Hmm"]
    count = 0
    for prefix in friendly_prefixes:
        count += len(re.findall(re.escape(prefix), text, flags=re.IGNORECASE))
    sentences = split_sentences(text)
    score = count / (len(sentences) + 1)
    return clamp(score) 