import json
import datetime
import re

# Load knowledge base
with open("knowledge_base.json", "r") as file:
    knowledge_base = json.load(file)

def log_conversation(user, bot):
    with open("chat_log.txt", "a") as log:
        log.write(f"{datetime.datetime.now()}\n")
        log.write(f"User: {user}\n")
        log.write(f"Bot: {bot}\n\n")

def get_response(user_input):
    user_input = user_input.lower()

    # Greeting intent
    for pattern in knowledge_base["greetings"]:
        if re.search(pattern, user_input):
            return knowledge_base["responses"]["greeting"]

    # Help intent
    for pattern in knowledge_base["help"]:
        if re.search(pattern, user_input):
            return knowledge_base["responses"]["help"]

    # Small talk
    for pattern in knowledge_base["small_talk"]:
        if re.search(pattern, user_input):
            return knowledge_base["responses"]["small_talk"]

    # Domain knowledge
    for key, value in knowledge_base["domain"].items():
        if key in user_input:
            return value

    return "Sorry, I don't understand that. Can you rephrase?"

def chatbot():
    print("🤖 Simple Rule-Based Chatbot")
    print("Type 'exit' to quit\n")

    while True:
        user_input = input("You: ")

        if user_input.lower() == "exit":
            print("Bot: Goodbye! 👋")
            break

        bot_response = get_response(user_input)
        print("Bot:", bot_response)

        log_conversation(user_input, bot_response)

if __name__ == "__main__":
    chatbot()
