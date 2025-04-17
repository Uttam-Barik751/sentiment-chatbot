import random

responses = {
    "hello": ["Hi there!", "Hello!", "Hey! 👋"],
    "how are you": ["I'm good, thanks!", "Doing great, and you?", "All good!"],
    "bye": ["Goodbye!", "See you later!", "Bye! 👋"],
    "what type of boy is ankit singh":["he is pure lol!"],
    "default": ["I'm not sure I understand. Could you rephrase? 🤔"]
}

def simple_chatbot(user_input):
    user_input = user_input.lower()

    for key in responses:
        if key in user_input:
            return random.choice(responses[key])
    return random.choice(responses["default"])