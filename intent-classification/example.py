import os
from model import classify_intent


# Example conversations to test intent classification
test_conversations = [
    # Reset password intent
    [
        {"role": "user", "content": "I forgot my password and can't log in."},
        {"role": "assistant", "content": "I'm sorry to hear that. I can help you reset your password."},
        {"role": "user", "content": "Yes please, I need to reset it right away."}
    ],
    
    # Technical support intent
    [
        {"role": "user", "content": "My application keeps crashing when I try to upload files."},
        {"role": "assistant", "content": "I'm sorry to hear that. Can you tell me what type of files you're trying to upload?"},
        {"role": "user", "content": "Just regular PDFs, but it crashes every time. I've tried restarting the app."}
    ],
    
    # Product inquiry intent
    [
        {"role": "user", "content": "Do you offer a premium plan with additional features?"},
        {"role": "assistant", "content": "Yes, we do offer premium plans. Would you like to know more about them?"},
        {"role": "user", "content": "Yes, I'd like to know the pricing and what features are included."}
    ]
]

def main():
    # Check if OPENAI_API_KEY is set

    if not os.getenv("OPENAI_API_KEY"):
        print("Error: OPENAI_API_KEY environment variable is not set.")
        print("Please set your OpenAI API key as an environment variable or in a .env file.")
        return
    
    print("Intent Classification Examples\n")
    
    for i, conversation in enumerate(test_conversations, 1):
        print(f"\nExample {i}:")
        print("Conversation:")
        for message in conversation:
            role = message["role"]
            content = message["content"]
            print(f"  {role.capitalize()}: {content}")
        
        try:
            # Classify the intent
            result = classify_intent(conversation)
            
            # Print the results
            print("\nClassification Results:")
            print(f"  Explanation: {result.explanation}")
            print(f"  Intent: {result.intent}")
            print("-" * 80)
        except Exception as e:
            print(f"Error classifying intent: {e}")

if __name__ == "__main__":
    main() 