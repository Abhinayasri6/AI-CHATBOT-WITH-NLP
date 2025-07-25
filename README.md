# AI-CHATBOT-WITH-NLP

*COMPANY*:CODTECH IT SOLUTIONS

*NAME*:BASANI ABHINAYASRI

*INTERN ID*:CT04DH1512

*DOMAIN*:PYTHON PROGRAMMING

*DURATION*:4 WEEKS

*MENTOR*:NEELA SANTHOSH

*DESCRIPTION*:This chatbot project is built using Python and the spaCy library, aimed at creating a simple and intuitive conversation experience through the command line. At its core, the system relies on Natural Language Processing to interpret user inputs and match them with predefined conversational patterns. The key library used here is spaCy, which provides powerful features like tokenization and semantic similarity scoring. The model en_core_web_sm is loaded to process English text, and an optional command (python -m spacy download en_core_web_sm) is included to ensure it's available. Once initialized, the chatbot stores common phrases like “hello,” “bye,” or “how are you” as keys in a dictionary, each tied to a cheerful, emoji-enhanced response.
These phrases are converted into spaCy Doc objects so that when the user inputs something new, the system can compare the meaning of that input against known patterns. This is done using similarity() scoring, and if the best match crosses a threshold (set to 0.6), the bot replies with the corresponding response. Otherwise, it offers a fallback message showing curiosity and an echo of the user’s input. The chatbot runs in a continuous loop, where the user types in the terminal and exits with the command exit. Though simple, it cleverly combines rule-based interaction with semantic understanding. Additionally, sys is imported—often used for debugging or ensuring proper emoji rendering on certain systems. Overall, this project illustrates a neat fusion of user-friendly logic and modern NLP tools. With just a few lines of code, it builds the foundation for an expandable, intelligent assistant ready to be upgraded with additional features like voice input or GUI interfaces.
The chatbot operates inside a loop controlled by the chat() function. This loop continuously reads input from the user, checks if the exit condition (“exit”) is met, and otherwise prints the selected response. This allows for an uninterrupted conversational experience where the user can interact freely until they choose to end the session.
Additionally, the sys module is imported—though not actively used in the displayed code, it may serve future debugging or encoding fixes, especially when rendering emojis on diverse operating systems. Debugging output like print("DEBUG: Processing input:", user_input) provides transparency during development by showing what the chatbot is analyzing behind the scenes.

