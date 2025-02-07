
def chatbot_response(user_input):
    responses = {
        "hello": "Hi there!",
        "how are you": "I'm good, thank you!",
        "bye": "Goodbye!"
    }
    return responses.get(user_input.lower(), "I don't understand that.")

while True:
    user_input = input("You: ")
    if user_input.lower() == "bye":
        print("Chatbot: Goodbye!")
        break
    print(f"Chatbot: {chatbot_response(user_input)}")