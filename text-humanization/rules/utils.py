import re
import random

def clamp(value, minimum=0, maximum=1):
    """Clamp a value between a minimum and maximum."""
    return max(minimum, min(value, maximum))

def split_sentences(text):
    """Split text into sentences (simple split by punctuation)."""
    return re.split(r'(?<=[.!?])\s+', text) 