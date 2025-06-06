import nltk
from nltk.chat.util import Chat, reflections

# Download the required NLTK datasets (if not already installed)
nltk.download('punkt')

# Define a list of pairs that represent possible patterns and responses
pairs = [
    (r"hi|hello|hey", ["Hello! How can I help you today?", "Hey there! How can I assist you?"]),
    (r"how are you?", ["I'm doing great, thank you!", "I'm just a bot, but I'm functioning well!"]),
    (r"what is your name?", ["I am a chatbot created to assist you.", "I don't have a specific name, but you can call me Bot."]),
    (r"bye|goodbye", ["Goodbye! Have a great day!", "Bye! Take care!"]),
    (r"(.*) your (.*)", ["Why are you interested in my %2?", "What about my %2 would you like to know?"]),
    (r"(.*) (good|great|fine|well)", ["I'm glad to hear that!", "That's awesome!"]),
    (r"(.*) (help|support)", ["Sure, how can I assist you?", "What do you need help with?"]),
    (r"(.*)", ["Sorry, I didn't quite understand that.", "Can you please rephrase?"])
]

# Create the chatbot using the defined pairs and reflections
chatbot = Chat(pairs, reflections)

def start_chat():
    print("Hello! I am your chatbot. Type 'bye' to end the conversation.")
    print("How can I help you today?")
    
    # Start the conversation loop
    while True:
        user_input = input("You: ")
        
        if user_input.lower() in ['bye', 'goodbye']:
            print("Chatbot: Goodbye! Take care.")
            break
        
        response = chatbot.respond(user_input)
        print("Chatbot:", response)

if __name__ == "__main__":
    start_chat()
