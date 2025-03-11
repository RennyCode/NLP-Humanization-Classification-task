"""
Emoji Injection Rule

Purpose:  
Insert context-appropriate emojis to convey tone and emotion, adding a more personable, human feel.

Examples:  
- Example 1:  
  Input: "I love this idea!"  
  Output: "I love this idea! 😊"
- Example 2:  
  Input: "That's interesting."  
  Output: "That's interesting 🤔."
- Example 3:  
  Input: "Great job."  
  Output: "Great job! 👍"
"""

import random
import re
from rules.utils import clamp, split_sentences

def fix_emojis(text, injection_probability=0.3):
    """
    Append a context-appropriate emoji to sentences with a given probability.
    
    Args:
        text (str): The text to modify
        injection_probability (float): Probability of adding an emoji
        
    Returns:
        str: Modified text with emojis
    """
    # Dictionary of emoji categories
    emoji_categories = {
        "greeting": ["👋", "😊", "🙂", "👍"],
        "question": ["🤔", "❓", "👀"],
        "positive": ["✨", "💯", "🙌", "👏", "😊", "👍", "💪"],
        "negative": ["😔", "😕", "🤦‍♂️", "😬"],
        "surprise": ["😮", "😲", "😯", "😳"],
        "general": ["😎", "👍", "💫"]
    }
    
    sentences = split_sentences(text)
    new_sentences = []
    
    # Don't add emoji if there's already one
    emoji_pattern = re.compile("[\U0001F600-\U0001F64F\U0001F300-\U0001F5FF\U0001F680-\U0001F6FF]")
    if emoji_pattern.search(text):
        return text
    
    # For short greetings, only add emoji at the end of message
    if len(text.split()) <= 5 and re.search(r'^(hi|hey|hello|what\'s up|yo)\b', text, re.IGNORECASE):
        if random.random() < injection_probability:
            emoji = random.choice(emoji_categories["greeting"])
            # Add emoji at the end
            if text[-1] in ['.', '!', '?']:
                return text[:-1] + " " + emoji + text[-1]
            else:
                return text + " " + emoji
        return text
        
    for sentence in sentences:
        if sentence and random.random() < injection_probability:
            # Determine sentence type for context-appropriate emoji
            if "?" in sentence:
                emoji_type = "question"
            elif any(word in sentence.lower() for word in ["hi", "hey", "hello", "greetings", "howdy"]):
                emoji_type = "greeting"
            elif any(word in sentence.lower() for word in ["good", "great", "love", "awesome", "nice", "happy", "thanks", "thank you"]):
                emoji_type = "positive"
            elif any(word in sentence.lower() for word in ["bad", "sad", "sorry", "unfortunately", "problem", "issue", "wrong"]):
                emoji_type = "negative"
            elif any(word in sentence.lower() for word in ["wow", "amazing", "unbelievable", "can't believe", "incredible"]):
                emoji_type = "surprise"
            else:
                emoji_type = "general"
                
            emoji = random.choice(emoji_categories[emoji_type])
            
            # Add emoji at the end of the sentence
            if sentence[-1] in ['.', '!', '?']:
                sentence = sentence[:-1] + " " + emoji + sentence[-1]
            else:
                sentence = sentence + " " + emoji
        new_sentences.append(sentence)
    return " ".join(new_sentences)

def score_emojis(text):
    """
    Score the text based on emoji usage.
    
    Args:
        text (str): The text to score
        
    Returns:
        float: Score between 0 and 1
    """
    emoji_pattern = re.compile("[\U0001F600-\U0001F64F\U0001F300-\U0001F5FF\U0001F680-\U0001F6FF]")
    emojis_found = emoji_pattern.findall(text)
    sentences = split_sentences(text)
    
    if len(sentences) == 0:
        return 0
    
    score = len(emojis_found) / len(sentences)
    return clamp(score) 