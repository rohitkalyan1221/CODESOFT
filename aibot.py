def chatbot():
    print("Chatbot: Hi! I'm your assistant. How can I help you today?")
    
    while True:
        user_input = input("You: ").lower()

        if "hello" in user_input or "hi" in user_input:
            print("Chatbot: Hello there! How can I assist you?")
        
        elif "how are you" in user_input:
            print("Chatbot: I'm just a bunch of code, but thanks for asking! How can I help?")
        
        elif "your name" in user_input:
            print("Chatbot: I'm RuleBot, your simple chatbot assistant!")
        
        elif "help" in user_input:
            print("Chatbot: Sure! I can answer simple questions or just chat with you.")
        
        elif "bye" in user_input or "exit" in user_input:
            print("Chatbot: Goodbye! Have a great day.")
            break
        
        elif "time" in user_input:
            from datetime import datetime
            now = datetime.now()
            print(f"Chatbot: The current time is {now.strftime('%H:%M:%S')}")
        
        else:
            print("Chatbot: Sorry, I didn't understand that. Can you rephrase?")

# Run the chatbot
chatbot()
