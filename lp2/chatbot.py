import random

# Define the responses
GREETING_RESPONSES = ["Hello!", "Hi!", "Welcome!", "Hey there!"]
GOODBYE_RESPONSES = ["Goodbye!", "Bye!", "See you later!", "Take care!"]
THANKS_RESPONSES = ["You're welcome!", "No problem!", "Glad I could help!"]
UNKNOWN_RESPONSES = ["Sorry, I didn't understand that.", "I'm not sure what you mean.", "Could you please rephrase that?"]

# Function to generate a response based on user input
def generate_response(user_input):
    user_input = user_input.lower()
    
    if user_input.startswith(("hi", "hello", "hey")):
        return random.choice(GREETING_RESPONSES)
    elif user_input.startswith(("bye", "goodbye")):
        return random.choice(GOODBYE_RESPONSES)
    elif "thank you" in user_input:
        return random.choice(THANKS_RESPONSES)
    else:
        return random.choice(UNKNOWN_RESPONSES)

# Main interaction loop
def chat():
    print("ChatBot: Hello! How can I assist you today?")
    
    while True:
        user_input = input("User: ")
        response = generate_response(user_input)
        print("ChatBot:", response)
        
        if user_input.lower() == "exit":
            break

# Start the chat
chat()
