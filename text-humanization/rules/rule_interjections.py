"""
Interjection Insertion Rule

Purpose:  
Insert interjections (e.g., "oh", "wow", "oops") at natural breakpoints to enhance spontaneity.

Examples:  
- Example 1:  
  Input: "I forgot my keys."  
  Output: "Oh, I forgot my keys."
- Example 2:  
  Input: "That happened."  
  Output: "Wow, that happened."
- Example 3:  
  Input: "I didn't see that."  
  Output: "Oops, I didn't see that."
"""

import random
import re
from rules.utils import clamp, split_sentences

def fix_interjections(text, interjection_probability=0.2):
    """
    Insert interjections at the beginning of sentences.
    
    Args:
        text (str): The text to modify
        interjection_probability (float): Probability of inserting an interjection
        
    Returns:
        str: Text with interjections inserted
    """
    # Don't add interjections if they already exist
    interjections = ["Oh", "Wow", "Oops"]
    if any(interjection.lower() in text.lower() for interjection in interjections):
        return text
    
    # Skip greetings - don't add interjections to simple greetings
    if re.search(r'^(hi|hey|hello|what\'s up|yo)\b', text, re.IGNORECASE):
        return text
    
    # Context-appropriate interjections
    positive_patterns = [r'great', r'good', r'nice', r'awesome', r'amazing', r'love']
    negative_patterns = [r'bad', r'wrong', r'error', r'mistake', r'forgot', r'didn\'t', r'can\'t', r'problem']
    surprise_patterns = [r'surprising', r'unexpected', r'strange', r'weird', r'unusual']
        
    sentences = split_sentences(text)
    
    # Apply to at most one sentence
    if not sentences or random.random() >= interjection_probability:
        return text
        
    sentence_idx = random.randint(0, len(sentences) - 1)
    sentence = sentences[sentence_idx]
    
    # Choose contextually appropriate interjection
    if any(re.search(pattern, sentence, re.IGNORECASE) for pattern in positive_patterns):
        interjection = "Wow"
    elif any(re.search(pattern, sentence, re.IGNORECASE) for pattern in negative_patterns):
        interjection = "Oops"
    elif any(re.search(pattern, sentence, re.IGNORECASE) for pattern in surprise_patterns):
        interjection = random.choice(["Wow", "Oh"])
    else:
        interjection = random.choice(interjections)
    
    # Add interjection and maintain appropriate capitalization
    if sentence[0].isupper():
        sentences[sentence_idx] = interjection + ", " + sentence
    else:
        sentences[sentence_idx] = interjection.lower() + ", " + sentence
    
    return " ".join(sentences)

def score_interjections(text):
    """
    Score the text based on presence of interjections.
    
    Args:
        text (str): The text to score
        
    Returns:
        float: Score between 0 and 1
    """
    interjections = ["Oh", "Wow", "Oops"]
    count = 0
    for interjection in interjections:
        count += len(re.findall(r'\b' + re.escape(interjection) + r'\b', text, flags=re.IGNORECASE))
    sentences = split_sentences(text)
    score = count / (len(sentences) + 1)
    return clamp(score) 