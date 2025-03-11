"""
Capitalization Variation Rule

Purpose:  
Introduce slight, controlled deviations in standard capitalization to mimic natural human inconsistency 
(e.g., an occasional missed capital letter at the start of a sentence).

Examples:  
- Example 1:  
  Input: "I went to the store."  
  Output (if applying variation): "i went to the store."
- Example 2:  
  Input: "It's a sunny day."  
  Output: "it's a sunny day."
- Example 3:  
  Input: "Hello, how are you?"  
  Output: "hello, how are you?"
"""

import random
from rules.utils import clamp, split_sentences

def fix_capitalization(text, variation_level):
    """
    Introduce slight variations in capitalization.
    
    Args:
        text (str): The text to modify
        variation_level (float): Probability of applying lowercase to first letter
        
    Returns:
        str: Modified text with capitalization variations
    """
    sentences = split_sentences(text)
    new_sentences = []
    for sentence in sentences:
        if sentence:
            if random.random() < variation_level:
                sentence = sentence[0].lower() + sentence[1:]
            new_sentences.append(sentence)
    return " ".join(new_sentences)

def score_capitalization(text):
    """
    Score how many sentences start with lowercase.
    
    Args:
        text (str): The text to score
        
    Returns:
        float: Score between 0 and 1
    """
    sentences = split_sentences(text)
    errors = sum(1 for s in sentences if s and s[0].islower())
    if len(sentences) == 0:
        return 0
    score = errors / len(sentences)
    return clamp(score) 