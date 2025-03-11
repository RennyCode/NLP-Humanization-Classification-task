"""
Exclamation Mark Variation Rule

Purpose:  
Vary the number and placement of exclamation marks to mirror human emphasis (without overdoing it).

Examples:  
- Example 1:  
  Input: "Great."  
  Output: "Great!"
- Example 2:  
  Input: "Wow"  
  Output: "Wow!"
- Example 3:  
  Input: "Amazing"  
  Output: "Amazing!!"
"""

import random
import re
from rules.utils import clamp, split_sentences

def fix_exclamations(text, variation_factor=0.2):
    """
    Vary the number and placement of exclamation marks.
    
    Args:
        text (str): The text to modify
        variation_factor (float): Probability of adding/varying exclamation marks
        
    Returns:
        str: Text with varied exclamation marks
    """
    # Don't modify if already has exclamations
    if "!" in text:
        return text
        
    sentences = split_sentences(text)
    new_sentences = []
    for sentence in sentences:
        if sentence:
            if not any(c in sentence for c in "!?") and random.random() < variation_factor:
                sentence = sentence.rstrip(".") + "!"
            elif "!" in sentence and random.random() < variation_factor:
                count = random.choices([1,2], weights=[0.8,0.2])[0]
                sentence = re.sub(r'!+', "!" * count, sentence)
        new_sentences.append(sentence)
    return " ".join(new_sentences)

def score_exclamations(text):
    """
    Score the text based on presence of exclamation marks.
    
    Args:
        text (str): The text to score
        
    Returns:
        float: Score between 0 and 1
    """
    exclamations = text.count("!")
    sentences = split_sentences(text)
    score = exclamations / (len(sentences) + 1)
    return clamp(score) 