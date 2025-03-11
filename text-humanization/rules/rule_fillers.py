"""
Fillers Injection Rule

Purpose:  
Inject filler words or phrases (e.g., "um", "uh", "you know") at appropriate points to simulate the natural pauses or hesitations in human speech.

Examples:  
- Example 1:  
  Input: "I went to the store."  
  Output: "I, um, went to the store."
- Example 2:  
  Input: "That was amazing."  
  Output: "That was, you know, amazing."
- Example 3:  
  Input: "Let's start."  
  Output: "Let's, uh, start."
"""

import random
import re
from rules.utils import clamp, split_sentences

def fix_fillers(text, filler_probability=0.2):
    """
    Inject filler words into text to simulate natural speech hesitation.
    
    Args:
        text (str): The text to modify
        filler_probability (float): Probability of adding a filler
        
    Returns:
        str: Modified text with fillers
    """
    # Don't add fillers if they already exist
    fillers = ["um", "uh", "you know"]
    if any(filler in text.lower() for filler in fillers):
        return text
        
    sentences = split_sentences(text)
    new_sentences = []
    for sentence in sentences:
        words = sentence.split()
        if len(words) > 3 and random.random() < filler_probability:
            filler = random.choice(fillers)
            # Insert the filler after the first word.
            words.insert(1, filler)
            sentence = " ".join(words)
        new_sentences.append(sentence)
    return " ".join(new_sentences)

def score_fillers(text):
    """
    Score the text based on presence of filler words.
    
    Args:
        text (str): The text to score
        
    Returns:
        float: Score between 0 and 1
    """
    filler_count = len(re.findall(r'\b(um|uh|you know)\b', text.lower()))
    sentences = split_sentences(text)
    score = filler_count / (len(sentences) + 1)
    return clamp(score) 