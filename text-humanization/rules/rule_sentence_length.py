"""
Sentence Length Variation Rule

Purpose:  
Modify sentence boundaries by merging or splitting sentences to vary length, imitating the irregular flow of human thought.

Examples:  
- Example 1:  
  Input: "I went to the store. I bought milk."  
  Output: "I went to the store, and I bought milk."
- Example 2:  
  Input: "It's raining. I stayed inside."  
  Output: "It's raining; I stayed inside."
- Example 3:  
  Input: "I love coding. It's fun."  
  Output: "I love coding—it's fun."
"""

import random
from rules.utils import clamp, split_sentences

def fix_sentence_length(text, merge_probability=0.2):
    """
    Modify sentence boundaries to create more varied sentence lengths.
    
    Args:
        text (str): The text to modify
        merge_probability (float): Probability of merging two sentences
        
    Returns:
        str: Text with varied sentence lengths
    """
    sentences = split_sentences(text)
    
    # If there's only one sentence or it's already short, don't modify
    if len(sentences) <= 1 or len(text) < 40:
        return text
        
    new_sentences = []
    i = 0
    while i < len(sentences):
        if i < len(sentences) - 1 and random.random() < merge_probability:
            connector = random.choice([", and", ";", "—"])
            # Merge two sentences with a connector; lowercase the first letter of the second sentence.
            second_sent = sentences[i+1]
            if second_sent and second_sent[0].isupper():
                second_sent = second_sent[0].lower() + second_sent[1:]
                
            merged = sentences[i].rstrip(".!?") + connector + " " + second_sent
            new_sentences.append(merged)
            i += 2
        else:
            new_sentences.append(sentences[i])
            i += 1
    return " ".join(new_sentences)

def score_sentence_length(text):
    """
    Score the text based on sentence length variation.
    
    Args:
        text (str): The text to score
        
    Returns:
        float: Score between 0 and 1
    """
    sentences = split_sentences(text)
    lengths = [len(s.split()) for s in sentences if s]
    
    if len(lengths) <= 1:
        return 0
        
    avg = sum(lengths) / len(lengths)
    variance = sum((l - avg)**2 for l in lengths) / len(lengths)
    threshold = 10  # arbitrary threshold for variance
    score = min(variance / threshold, 1)
    return score 