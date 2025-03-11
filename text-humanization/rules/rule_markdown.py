"""
Remove Markdown Formatting Rule

Purpose:  
Strip out markdown syntax (e.g., bold, italics, headers, links) to present plain text that appears more natural in casual conversation.

Examples:  
- Example 1:  
  Input: "This is **bold** text."  
  Output: "This is bold text."
- Example 2:  
  Input: "Visit [this link](http://example.com)"  
  Output: "Visit this link"
- Example 3:  
  Input: "# Heading"  
  Output: "Heading"
"""

import re
from rules.utils import clamp

def fix_remove_markdown(text):
    """
    Remove Markdown formatting from text.
    
    Args:
        text (str): The text to modify
        
    Returns:
        str: Text with markdown formatting removed
    """
    text = re.sub(r"\*\*(.*?)\*\*", r"\1", text)   # Bold
    text = re.sub(r"\*(.*?)\*", r"\1", text)       # Italics
    text = re.sub(r"\[(.*?)\]\(.*?\)", r"\1", text)   # Links
    text = re.sub(r"^\s*#+\s*", "", text, flags=re.MULTILINE)  # Headers
    return text

def score_remove_markdown(text):
    """
    Score the text based on presence of markdown syntax.
    
    Args:
        text (str): The text to score
        
    Returns:
        float: Score between 0 and 1
    """
    markdown_syntax = len(re.findall(r"(\*\*.*?\*\*|\*.*?\*|\[.*?\]\(.*?\)|^\s*#+\s*)", text))
    
    if len(text) == 0:
        return 0
        
    score = markdown_syntax / len(text)
    return clamp(score) 