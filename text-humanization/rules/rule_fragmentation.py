"""
Sentence Fragmentation Rule

Purpose:  
Introduce sentence fragments or ellipses to simulate natural, spoken language and spontaneous thought.

Examples:  
- Example 1:  
  Input: "I was thinking about what you said."  
  Output: "I was thinking... about what you said."
- Example 2:  
  Input: "Went to the store. Got milk."  
  Output: "Went to the store, got milk."
- Example 3:  
  Input: "Really enjoyed it. Very much."  
  Output: "Really enjoyed it, very much."
"""

import random
from rules.utils import clamp, split_sentences

def fix_fragmentation(text, fragmentation_probability=0.15):
    """
    Introduce sentence fragments or ellipses.
    
    Args:
        text (str): The text to modify
        fragmentation_probability (float): Probability of fragmenting sentences
        
    Returns:
        str: Text with sentence fragmentation
    """
    # Don't apply fragmentation to short text
    if len(text) < 40:
        return text
        
    # Don't apply if already contains ellipsis
    if "..." in text:
        return text
        
    sentences = split_sentences(text)
    result = []
    i = 0
    
    # Apply to at most one part of the text
    fragmented = False
    
    while i < len(sentences):
        if not fragmented and i < len(sentences) - 1 and len(sentences[i].split()) < 5 and len(sentences[i+1].split()) < 5 and random.random() < fragmentation_probability:
            connector = random.choice([", ", "... ", " - ", "; "])
            # Lowercase the first letter of the second sentence if needed
            second_sent = sentences[i+1]
            if second_sent and second_sent[0].isupper():
                second_sent = second_sent[0].lower() + second_sent[1:]
                
            combined = sentences[i].rstrip(".!?") + connector + second_sent
            result.append(combined)
            i += 2
            fragmented = True
        elif not fragmented and len(sentences[i]) > 40 and random.random() < fragmentation_probability:
            parts = sentences[i].split(",")
            if len(parts) > 1:
                break_point = random.randint(1, len(parts)-1)
                first_part = ",".join(parts[:break_point]).rstrip(".!?")
                second_part = ",".join(parts[break_point:]).strip()
                result.append(first_part + "...")
                result.append(second_part)
                fragmented = True
            else:
                result.append(sentences[i])
            i += 1
        else:
            result.append(sentences[i])
            i += 1
    return " ".join(result)

def score_fragmentation(text):
    """
    Score the text based on presence of ellipses.
    
    Args:
        text (str): The text to score
        
    Returns:
        float: Score between 0 and 1
    """
    ellipsis_count = text.count("...")
    sentences = split_sentences(text)
    score = ellipsis_count / (len(sentences) + 1)
    return clamp(score) 