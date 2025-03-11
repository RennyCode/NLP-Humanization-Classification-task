import argparse
import random
from rules import rules  # Import the modular rules from the rules package


def humanize_text(text, debug=False):
    """Apply all humanization rules to the text and return the result."""
    original_text = text
    
    if debug:
        print("Original text:", original_text)
        print("=" * 50)
    
    # For short texts, limit the number of transformations applied
    text_length = len(text.split())
    
    # Define how many rules to apply based on text length
    if text_length <= 5:  # Very short text (like greetings)
        max_transformations = 1  # Apply at most 1 transformation
    elif text_length <= 15:  # Short text
        max_transformations = 2  # Apply at most 2 transformations
    else:  # Longer text
        max_transformations = len(rules)  # Apply all rules
    
    transformations_applied = 0
    
    # Apply each rule sequentially, considering their weights.
    for i, (rule_name, fix_func, score_func, params, weight) in enumerate(rules, start=1):
        # Use the rule's weight to determine if it should be applied
        if random.random() > weight:
            if debug:
                print(f"Rule {i}: {rule_name} - SKIPPED (weight: {weight})")
                print("-" * 50)
            continue
            
        old_text = text
        text = fix_func(text, **params) if params else fix_func(text)
        
        # Count this as a transformation only if the text changed
        if old_text != text:
            transformations_applied += 1
            
        score = score_func(text)
        
        if debug:
            print(f"Rule {i}: {rule_name} (weight: {weight})")
            print(f"Score: {score:.2f}")
            print(f"Output: {text}")
            print("-" * 50)
            
        # Stop if we've reached the maximum number of transformations for this text length
        # EXCEPT for rules with weight=1.0 which should always run
        if transformations_applied >= max_transformations and weight < 1.0:
            if debug:
                print(f"Stopped after applying {transformations_applied} transformations (max for this text length)")
            break
    
    if debug:
        print("Final output after all rules applied:")
        print(text)
    
    return text

def main():
    parser = argparse.ArgumentParser(description="Humanize text output by applying a set of rules.")
    parser.add_argument("--input", type=str, required=True, help="Input text to be humanized")
    parser.add_argument("--debug", action="store_true", help="Enable debug output")
    parser.add_argument("-n", "--num-runs", type=int, default=15, help="Number of times to run humanization")
    args = parser.parse_args()

    # Process the input text
    original_text = args.input
    
    # Run humanization multiple times if requested
    results = []
    for i in range(args.num_runs):
        if args.debug and args.num_runs > 1:
            print(f"\nRun {i+1}/{args.num_runs}:")
            print("-" * 20)
        
        result = humanize_text(original_text, debug=args.debug)
        results.append(result)
        
        # Print result for each run
        if args.num_runs > 1:
            print(f"Run {i+1}: {result}")
    
    # If only one run, just print the result without the "Run: " prefix
    if args.num_runs == 1:
        print(results[0])
    

if __name__ == "__main__":
    main()
