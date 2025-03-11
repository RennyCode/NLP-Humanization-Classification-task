"""
Sentence Structure Variation Rule

Purpose:  
Reorder clauses or restructure sentences (without changing meaning) to mimic the variety found in human expression.

Examples:  
- Example 1:  
  Input: "I am happy because it is sunny."  
  Output: "Because it's sunny, I am happy."
- Example 2:  
  Input: "I like ice cream because it tastes good."  
  Output: "Because it tastes good, I like ice cream."
- Example 3:  
  Input: "I went home because it was late."  
  Output: "It was late, so I went home."
"""

import re
from rules.utils import clamp, split_sentences

def fix_sentence_structure(text):
    """
    Reorder clauses in sentences containing "because" to create more varied sentence structures.
    
    Args:
        text (str): The text to modify
        
    Returns:
        str: Text with varied sentence structures
    """
    # Only apply if the sentence contains "because"
    if "because" not in text.lower():
        return text
        
    sentences = split_sentences(text)
    new_sentences = []
    for sentence in sentences:
        if "because" in sentence.lower():
            parts = re.split(r'\bbecause\b', sentence, flags=re.IGNORECASE)
            if len(parts) == 2:
                # Rearrange: move the clause after "because" to the beginning.
                second_part = parts[1].strip()
                if second_part and second_part[0].islower():
                    second_part = second_part[0].upper() + second_part[1:]
                sentence = second_part + ", so " + parts[0].strip().lower()
        new_sentences.append(sentence)
    return " ".join(new_sentences)

def score_sentence_structure(text):
    """
    Score the text based on the presence of sentences with "because".
    
    Args:
        text (str): The text to score
        
    Returns:
        float: Score between 0 and 1
    """
    count = len(re.findall(r'\bbecause\b', text, flags=re.IGNORECASE))
    ideal_variant_count = 1  # arbitrary
    score = min(count / ideal_variant_count, 1)
    return score 