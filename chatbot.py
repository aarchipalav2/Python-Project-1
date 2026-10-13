
def chatbot():
    print("===== Welcome to Python Chatbot =====")
    print("Type 'bye' to exit the chatbot.")

    while True:
        user_input = input("\nYou: ").lower().strip()

        if user_input in ["hello", "hi", "hey"]:
            print("Bot: Hello! How can I help you?")

        elif user_input == "how are you":
            print("Bot: I am fine! Thank you for asking.")

        elif user_input in ["what is your name", "who are you"]:
            print("Bot: I am a simple Python chatbot.")

        elif user_input in ["thanks", "thank you"]:
            print("Bot: You're welcome!")

        elif user_input in ["bye", "exit", "quit"]:
            print("Bot: Goodbye! Have a nice day!")
            break

        else:
            print("Bot: Sorry, I don't understand that message.")


chatbot()