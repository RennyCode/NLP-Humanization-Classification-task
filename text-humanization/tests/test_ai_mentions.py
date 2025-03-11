import pytest
from rules.rule_ai_mentions import fix_ai_mentions, score_ai_mentions, ai_phrases

# Test the fix_ai_mentions function
def test_remove_ai_mentions():
    """Test that AI mentions are removed from text."""
    test_cases = [
        ("As an AI, I think this is interesting.", "I think this is interesting."),
        ("I'm an AI assistant, I can help you.", "I can help you."),
        ("Hello, I'm an AI created by OpenAI.", "Hello,."),
        ("AI Assistant can answer your questions.", "can answer your questions.")
    ]
    
    for input_text, expected in test_cases:
        assert fix_ai_mentions(input_text) == expected

def test_case_insensitivity():
    """Test that AI mention removal is case insensitive."""
    test_cases = [
        ("as an ai, I think", "I think"),
        ("i'm an ai assistant, I can help", "I can help"),
        ("AS AN AI, I cannot", "I cannot")
    ]
    
    for input_text, expected in test_cases:
        assert fix_ai_mentions(input_text) == expected

def test_multiple_mentions():
    """Test removing multiple AI mentions in the same text."""
    text = "As an AI, I think. I'm an AI assistant, so I can help. As an AI, I have limitations."
    expected = "I think. so I can help. I have limitations."
    assert fix_ai_mentions(text) == expected

def test_no_ai_mentions():
    """Test that text without AI mentions remains unchanged."""
    text = "I think this is a good idea. Let me help you with that."
    assert fix_ai_mentions(text) == text

# Test the score_ai_mentions function
def test_score_with_no_mentions():
    """Test that text with no AI mentions gets a score of 0."""
    text = "This text has no AI mentions at all."
    assert score_ai_mentions(text) == 0

def test_score_with_mentions():
    """Test that text with AI mentions gets a score greater than 0."""
    text = "As an AI, I think this is interesting."
    score = score_ai_mentions(text)
    assert score > 0
    assert score <= 1.0
    
    # More mentions should result in a higher score
    text_with_more = "As an AI, I think. I'm an AI. As an AI Assistant, I know."
    assert score_ai_mentions(text_with_more) > score

def test_empty_text():
    """Test that empty text is handled correctly."""
    assert fix_ai_mentions("") == ""
    assert score_ai_mentions("") == 0

# Test AI company and model name removal
def test_remove_ai_company_model_names():
    """Test that AI company and model names are removed from text."""
    test_cases = [
        ("I am running on ChatGPT technology.", "I am running on technology."),
        ("Anthropic has developed this assistant.", "has developed this assistant."),
        ("Claude is helping you today.", "is helping you today."),
        ("This uses GPT-4 architecture.", "This uses architecture."),
        ("Created by OpenAI to help users.", "to help users.")
    ]
    
    for input_text, expected in test_cases:
        assert fix_ai_mentions(input_text) == expected

def test_case_insensitivity_company_models():
    """Test that AI company and model name removal is case insensitive."""
    test_cases = [
        ("powered by openai", "powered by"),
        ("using CHATGPT for this task", "using for this task"),
        ("claude can assist you", "can assist you")
    ]
    
    for input_text, expected in test_cases:
        assert fix_ai_mentions(input_text) == expected

# Parametrized test showing how to test multiple cases efficiently in pytest
@pytest.mark.parametrize("ai_phrase", ai_phrases)
def test_individual_phrases(ai_phrase):
    """Test each AI phrase individually is removed."""
    text = f"{ai_phrase} this is a test."
    expected = "this is a test."
    assert fix_ai_mentions(text) == expected 