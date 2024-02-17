import nltk
from nltk.chat.util import Chat, reflections

patterns = [
    (r'hi|hello|hey', ['Hi there!', 'Hello!', 'Hey!']),
    (r'how are you', ['I am good, thank you.', 'I am doing well. How about you?']),
    (r'(.*) your name', ['I am a chatbot. You can call me ChatGPT.', 'I am ChatGPT, your virtual assistant.']),
    (r'bye|goodbye', ['Goodbye!', 'Have a great day!', 'See you later.']),
    (r'who are you', ['i am a chat bot!!']),
    (r'(.*)', ['Sorry, I did not understand that.', 'I am still learning. Can you please rephrase?'])
]

chatbot = Chat(patterns, reflections)


def start_chat():
    print("Hi! I'm your chatbot. Ask me anything or say goodbye to end the conversation.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'bye':
            print("Chatbot: Goodbye!")
            break
        response = chatbot.respond(user_input)
        print("Chatbot:", response)


start_chat()
