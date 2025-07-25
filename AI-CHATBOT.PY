import spacy
import sys

# Load English NLP model
# You might need to download the model the first time you run this:
# !python -m spacy download en_core_web_sm

nlp = spacy.load("en_core_web_sm")

# Predefined patterns and responses
PATTERNS = {
    "hello": "👋 Hi there! What can I do for you today?",
    "your name": "🤖 I'm your trusty NLP-powered chatbot!",
    "bye": "👋 See you later! Take care.",
    "how are you": "⚡ I'm feeling charged up and ready!",
}

# Convert patterns to Doc objects
pattern_docs = {nlp(text): response for text, response in PATTERNS.items()}

def chatbot_response(user_input):
    user_doc = nlp(user_input.lower())
    print("DEBUG: Processing input:", user_input)
    best_match = None
    highest_score = 0.0

    # Compare input to each pattern using similarity
    for pattern_doc, response in pattern_docs.items():
        score = user_doc.similarity(pattern_doc)
        if score > highest_score:
            highest_score = score
            best_match = response

    # Set a threshold to catch vague inputs
    if highest_score > 0.6:
        return best_match
    else:
        return "😅 I'm not quite sure what you mean, but I'm eager to learn more!"

def chat():
    print("🤖 Chatbot is online! Type 'exit' to quit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Chatbot: Exiting the chat. Goodbye!")
            break
        response = chatbot_response(user_input)


        # If chatbot is unsure, fall back to echo-style response
        if response.startswith("😅"):
            print(f"Chatbot: I heard you say \"{user_input}\"")
        else:
            print(f"Chatbot: {response}")
