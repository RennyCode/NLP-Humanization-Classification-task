"""
Minor Typos Introduction Rule

Purpose:  
Occasionally introduce minor, non-disruptive typos to emulate human imperfection without sacrificing meaning.

Examples:  
- Example 1:  
  Input: "Hello"  
  Output: "Helo" (removed letter)
- Example 2:  
  Input: "Friend"  
  Output: "Frined" (swapped letters)
- Example 3:  
  Input: "Great"  
  Output: "Grate" (replaced letter)
"""

import random
from rules.utils import clamp

def fix_typos(text, typo_probability=0.1):
    """
    Introduce minor, non-disruptive typos to text.
    
    Args:
        text (str): The text to modify
        typo_probability (float): Probability of introducing a typo to a word
        
    Returns:
        str: Text with minor typos introduced
    """
    words = text.split()
    new_words = []
    
    # Don't introduce typos if the text is already short
    if len(words) < 5:
        return text
        
    for word in words:
        if len(word) > 3 and random.random() < typo_probability:
            typo_type = random.choice(["remove", "swap"])
            if typo_type == "remove" and len(word) > 4:
                pos = random.randint(1, len(word)-2)
                word = word[:pos] + word[pos+1:]  # remove one letter
            elif typo_type == "swap" and len(word) > 3:
                pos = random.randint(1, len(word)-2)
                word = word[:pos] + word[pos+1] + word[pos] + word[pos+2:]  # swap two letters
        new_words.append(word)
    return " ".join(new_words)

def score_typos(text):
    """
    Score the text based on presence of typos.
    Note: This is a simplified implementation.
    
    Args:
        text (str): The text to score
        
    Returns:
        float: Score between 0 and 1
    """
    # Simple estimate of typos based on dictionary check (simplified here)
    words = text.split()
    typo_count = sum(1 for word in words if len(word) < 3)
    score = typo_count / (len(words) + 1)
    return clamp(score) 