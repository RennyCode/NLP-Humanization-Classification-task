import csv
import json
import time
from model import classify_intent
from sklearn.metrics import classification_report
import pandas as pd
import numpy as np

def load_test_dataset(file_path):
    """
    Load the test dataset from a JSON file.
    
    Args:
        file_path: Path to the JSON file containing conversations and expected intents
        
    Returns:
        A list of tuples (conversation, expected_intent)
    """
    dataset = []
    with open(file_path, 'r') as jsonfile:
        data = json.load(jsonfile)
        for item in data:
            conversation = item['conversation']
            expected_intent = item['expected_intent']
            dataset.append((conversation, expected_intent))
    
    return dataset

def evaluate_model(dataset):
    """
    Evaluate the intent classification model on the test dataset.
    
    Args:
        dataset: List of tuples (conversation, expected_intent)
        
    Returns:
        DataFrame with results containing predicted and expected intents
    """
    results = []
    
    for i, (conversation, expected_intent) in enumerate(dataset):
        try:
            # Classify the intent
            result = classify_intent(conversation)
            
            # Convert the Intent enum to its name for comparison
            predicted_intent_name = result.intent.name
            
            # Store results
            results.append({
                'conversation': json.dumps(conversation),
                'expected_intent': expected_intent,
                'predicted_intent': predicted_intent_name,
                'explanation': result.explanation,
                'is_correct': expected_intent == predicted_intent_name
            })
            
            # Print progress
            print(f"Sample {i+1}/{len(dataset)}: Expected={expected_intent}, Predicted={predicted_intent_name}, Correct={expected_intent == predicted_intent_name}")
            
        except Exception as e:
            print(f"Error processing sample {i}: {e}")
            # Add the error to results
            results.append({
                'conversation': json.dumps(conversation),
                'expected_intent': expected_intent,
                'predicted_intent': 'ERROR',
                'explanation': str(e),
                'is_correct': False
            })
    
    return pd.DataFrame(results)

def calculate_metrics(results_df):
    """
    Calculate and print performance metrics.
    
    Args:
        results_df: DataFrame with results
        
    Returns:
        None (prints metrics to console)
    """
    # Calculate overall accuracy
    accuracy = results_df['is_correct'].mean() * 100
    print(f"\nOverall Accuracy: {accuracy:.2f}%")
    
    # Generate classification report
    expected = results_df['expected_intent'].values
    predicted = results_df['predicted_intent'].values
    
    # Filter out error cases
    valid_indices = predicted != 'ERROR'
    expected_valid = expected[valid_indices]
    predicted_valid = predicted[valid_indices]
    
    # Classification report
    print("\nClassification Report:")
    print(classification_report(expected_valid, predicted_valid))    
    
    # Collect errors
    error_cases = results_df[~results_df['is_correct']]
    if len(error_cases) > 0:
        print("\nIncorrect Classifications:")
        for _, row in error_cases.iterrows():
            print(f"Conversation: {row['conversation']}")
            print(f"Expected: {row['expected_intent']}, Predicted: {row['predicted_intent']}")
            print(f"Explanation: {row['explanation']}")
            print("-" * 80)
    

def main():
    """Run the model evaluation"""
    print("Loading test dataset...")
    dataset = load_test_dataset('./intent-classification/test_dataset.json')
    print(f"Loaded {len(dataset)} samples.")
    
    print("\nEvaluating model performance...")
    results = evaluate_model(dataset)
    
    print("\nCalculating metrics...")
    calculate_metrics(results)

if __name__ == "__main__":
    main() 