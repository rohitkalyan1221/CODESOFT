def chatbot():
    print("🤖 Hello! I'm ChatBot. Type 'bye' to exit.")
    
    while True:
        user_input = input("You: ").lower()

        if user_input in ["hi", "Hi", "Hello", "hello", "Hey", "hey"]:
            print("Bot: Hello there! How can I help you?")
        
        elif "What is your name" in user_input:
            print("Bot: I'm a simple rule-based chatbot created in Python.")
        
        elif "how are you" in user_input:
            print("Bot: I'm doing great! Thanks for asking.")
        
        elif "tell me what is the time" in user_input:
            from datetime import datetime
            now = datetime.now().strftime("%H:%M:%S")
            print(f"Bot: The current time is {now}")
        
        elif "tell me today's date" in user_input:
            from datetime import date
            today = date.today()
            print(f"Bot: Today's date is {today}")
        
        elif "I need your help" in user_input:
            print("Bot: I can help you with basic info like time, date, greetings, and more!")
        
        elif "bye" in user_input or "exit" in user_input:
            print("Bot: Goodbye! Have a great day! 👋")
            break
        
        else:
            print("Bot: I'm not sure how to respond to that. Can you rephrase?")

chatbot()
