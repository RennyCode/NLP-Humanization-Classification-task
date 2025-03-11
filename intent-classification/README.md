# Intent Classification Testing

This project tests an intent classification model that categorizes user messages into predefined intents using OpenAI's API.

## Files

- `model.py`: The core intent classification model that uses OpenAI to classify user intents
- `test_dataset.json`: A dataset of 100 sample conversations with their expected intents
- `test_model.py`: Script to evaluate the model's performance against the test dataset

## Intent Categories

The model classifies user messages into several intent categories, including:

- Conversation management: `START_CONVERSATION`, `END_CONVERSATION`, `GREET`, `THANK`, etc.
- Information seeking: `ASK_GENERAL_QUESTION`, `ASK_TECHNICAL_SUPPORT`, `ASK_FOR_INFORMATION`, etc.
- Actions and requests: `REQUEST_ASSISTANCE`, `REQUEST_FEATURE`, `REQUEST_HUMAN`, etc.
- Account management: `CREATE_ACCOUNT`, `UPDATE_ACCOUNT`, `DELETE_ACCOUNT`, etc.
- Commerce: `PLACE_ORDER`, `CANCEL_ORDER`, `TRACK_ORDER`, etc.
- Scheduling: `BOOK_APPOINTMENT`, `CANCEL_APPOINTMENT`, `RESCHEDULE_APPOINTMENT`, etc.

## Pre running Steps:

1. Ensure you have the required dependencies installed:
   ```
   uv sync
   ```

2. Set your OpenAI API key as an environment variable:
   ```
   export OPENAI_API_KEY=your_api_key_here
   ```

## Running the Example

To see the intent classification model in action with a few sample conversations:

   Run the test script:
   ```
   uv run intent-classification/example.py
   ```

This will run three example conversations through the model and display the classified intent for each one.

## Running the Tests

   Run the test script:
   ```
   uv run intent-classification/test_model.py
   ```

## Test Metrics

The test script will generate the following metrics:

- Overall accuracy
- Classification report (precision, recall, f1-score)
- Confusion matrix
- List of incorrectly classified examples
