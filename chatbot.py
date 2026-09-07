#=======================================
#project_1: Rule-Based AI chatbot
#=======================================
print('='*50)
print('WELCOME TO AI CHATBOT')
print('='*50)

print('Hello! I am a rule-based AI chatbot.')
print('I can answer your questions based on predefined rules.')
print("Type 'exit','bye',or 'quit'to end the conversation.\n")

while True:
    user_input=input("You: ").lower().strip()

    if user_input in['bye','exit','quit']:
        print("chatbot: Goodbye! Have a great day!")
        break

    elif user_input in['hello','hye','hii','hi']:
        print("Chatbot: Hello! How can I assist you today?")

    elif user_input in["who are you","who are you?","what is your name","what is your name?"]:
        print("Chatbot: I am a rule-based AI chatbot created to assist you.")

    elif user_input in["how are you","how are you?"]:
        print("Chatbot: I'm just a program, but I'm functioning as expected! How can I help you?")

    elif "what is ai" in user_input or "what is artificial intelligence"in user_input:
        print("Chatbot: Artificial Intelligence (AI) is the simulation of human intelligence in machines that are programmed to think and learn like humans.")

    elif "what is ml" in user_input or "what is machine learning?" in user_input:
        print("Chatbot: Machine Learning is a subset of AI that enables systems to learn and improve from experience without being explicitly programmed.") 

    elif "how do you work" in user_input or "how do you work?" in user_input:
        print("Chatbot: I work based on predefined rules and patterns. I analyze your input and respond with the most appropriate answer from my knowledge base.")

    elif "help" in user_input or "can you help me" in user_input:
        print("Chatbot: Of course! Please ask your question, and I'll do my best to assist you.")

    elif "thank you" in user_input or "thanks" in user_input:
        print("Chatbot: You're welcome! If you have any more questions, feel free to ask.")

    else:
        print("Chatbot: I'm sorry, I don't have an answer for that. Please try asking something else or check my knowledge base.")
        
print("\nThank you for chatting with me! Goodbye!")


