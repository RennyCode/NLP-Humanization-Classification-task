"""
Excessive AI Mention Removal Rule

Purpose:
Strip out phrases that explicitly reference the model's AI nature (e.g., "as an AI") to avoid breaking the illusion of human conversation.

Examples:
- Example 1:
  Input: "As an AI, I think"
  Output: "I think"
- Example 2:
  Input: "As an AI, I cannot"
  Output: "I cannot"
- Example 3:
  Input: "I'm an AI."
  Output: ""
"""

from rules.utils import clamp, split_sentences
import re

ai_phrases = [
    "I'm an AI assistant,",
    "I'm an AI assistant",
    "As an AI Assistant,",
    "As an AI Assistant",
    "As an AI,",
    "I'm an AI",
    "As an artificial intelligence",
    "AI Assistant",
    # AI company and model names
    "OpenAI",
    "Anthropic",
    "Claude",
    "ChatGPT",
    "GPT-4",
    "GPT-3",
    "GPT",
    "created by OpenAI",
    "developed by Anthropic",
    "powered by Claude",
]


def fix_ai_mentions(text):
    """
    Remove phrases that explicitly reference the model's AI nature.
    Case insensitive matching is used.

    Args:
        text (str): The text to modify

    Returns:
        str: Text with AI mentions removed
    """
    # First handle the phrases with special characters like hyphens
    special_phrases = ["GPT-4", "GPT-3"]
    for phrase in special_phrases:
        pattern = re.compile(re.escape(phrase), re.IGNORECASE)
        text = pattern.sub("", text)
    
    # Handle complete phrases that contain "by" references
    complete_phrases = [
        "created by OpenAI",
        "developed by Anthropic",
        "powered by Claude"
    ]
    for phrase in complete_phrases:
        pattern = re.compile(re.escape(phrase), re.IGNORECASE)
        text = pattern.sub("", text)
    
    # Now handle the rest of the phrases
    for phrase in [p for p in ai_phrases if p not in special_phrases + complete_phrases]:
        pattern = re.compile(re.escape(phrase), re.IGNORECASE)
        text = pattern.sub("", text)
    
    # Clean up extra spaces that remain after removal
    text = re.sub(r'\s+', ' ', text)  # Replace multiple spaces with a single space
    text = text.strip()  # Remove leading and trailing spaces
    
    # Fix cases where punctuation has spaces before it
    text = re.sub(r'\s+([,.!?;:])', r'\1', text)
    
    return text


def score_ai_mentions(text):
    """
    Score the text based on presence of AI mentions.
    Case insensitive matching is used.

    Args:
        text (str): The text to score

    Returns:
        float: Score between 0 and 1
    """
    text_lower = text.lower()
    ai_count = sum(text_lower.count(phrase.lower()) for phrase in ai_phrases)
    sentences = split_sentences(text)
    score = ai_count / (len(sentences) + 1)
    return clamp(score)
