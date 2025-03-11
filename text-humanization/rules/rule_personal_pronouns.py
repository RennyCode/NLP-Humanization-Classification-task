"""
Personal Pronoun Emphasis Rule

Purpose:  
Increase the frequency of personal pronouns and first-person references (e.g., "I", "me") to create a more personable and conversational tone.

Examples:  
- Example 1:  
  Input: "The solution is effective."  
  Output: "I think the solution is effective."
- Example 2:  
  Input: "One might consider this option."  
  Output: "I would consider this option."
- Example 3:  
  Input: "It appears correct."  
  Output: "I feel it's correct."
"""

import random
import re
from rules.utils import clamp, split_sentences

def fix_personal_pronouns(text):
    """
    Increase the frequency of personal pronouns.
    
    Args:
        text (str): The text to modify
        
    Returns:
        str: Text with added personal pronouns
    """
    # Don't add if already contains personal pronouns
    if re.search(r'\b(I|me|my|mine)\b', text, flags=re.IGNORECASE):
        return text
    
    # Skip greetings - common greeting patterns
    greeting_patterns = [
        r'^hi\b', r'^hey\b', r'^hello\b', r'^what\'s up\b', r'^yo\b',
        r'^how are you', r'^how\'s it going', r'^good morning', r'^good afternoon', 
        r'^good evening', r'^howdy'
    ]
    for pattern in greeting_patterns:
        if re.search(pattern, text, re.IGNORECASE):
            return text
        
    sentences = split_sentences(text)
    
    # Apply to at most one sentence
    if not sentences:
        return text
        
    sentence_idx = random.randint(0, len(sentences) - 1)
    if sentences[sentence_idx]:
        if sentences[sentence_idx][0].isupper():
            sentences[sentence_idx] = "I think " + sentences[sentence_idx][0].lower() + sentences[sentence_idx][1:]
        else:
            sentences[sentence_idx] = "I think " + sentences[sentence_idx]
    
    return " ".join(sentences)

def score_personal_pronouns(text):
    """
    Score the text based on presence of personal pronouns.
    
    Args:
        text (str): The text to score
        
    Returns:
        float: Score between 0 and 1
    """
    count = len(re.findall(r'\b(I|me|my|mine)\b', text, flags=re.IGNORECASE))
    sentences = split_sentences(text)
    score = count / (len(sentences) + 1)
    return clamp(score) 