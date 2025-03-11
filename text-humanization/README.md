Simple:
```
python3 text-humanization/humanize_text.py --input="Hey, how are you?"
```

Simple:
```
python3 text-humanization/humanize_text.py --input="That's nice to hear. Is there anything specific you'd like to talk about or something I can help you with today?"
```

remove markdown and AI mentions:

```
python3 text-humanization/humanize_text.py --input="As an AI assistant, I can help you with a variety of tasks:\n* Answer questions and provide information on a wide range of topics\n* Help with writing tasks like drafting emails, essays, stories, or scripts\n* Summarize or explain complex concepts\n* Assist with creative brainstorming and idea generation"
```

```
python3 text-humanization/humanize_text.py --input="I'd be happy to help you with that question."
```

With debugging information:
```
python3 text-humanization/humanize_text.py --input="Let me look that up for you." --debug
```

## Common Chatbot Responses to Humanize

### Greeting and introduction:
```
python3 text-humanization/humanize_text.py --input="Hello! I'm an AI assistant. How can I help you today?"
```

### Asking for clarification:
```
python3 text-humanization/humanize_text.py --input="I'm not sure I understand what you're asking. Could you please provide more details or rephrase your question?"
```

### Answering a simple question:
```
python3 text-humanization/humanize_text.py --input="The capital of France is Paris. It's known as the City of Light and is famous for landmarks like the Eiffel Tower and the Louvre Museum."
```

### Providing a recommendation:
```
python3 text-humanization/humanize_text.py --input="Based on your preferences, I would recommend trying the new Italian restaurant on Main Street. They have excellent pasta dishes and a nice atmosphere for casual dining."
```

### Unable to fulfill a request:
```
python3 text-humanization/humanize_text.py --input="I apologize, but I don't have the ability to access external websites or browse the internet in real-time."
```

### Sympathetic response:
```
python3 text-humanization/humanize_text.py --input="I'm sorry to hear you're having a difficult day. That sounds really challenging, and it's understandable to feel frustrated in that situation."
```

### Continuation of a conversation:
```
python3 text-humanization/humanize_text.py --input="To continue from our previous discussion about gardening, here are some low-maintenance plants that would work well in your apartment with limited sunlight."
```

### run tests:

```
pytest
```