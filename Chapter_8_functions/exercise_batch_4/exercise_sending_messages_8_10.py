# Sending Messages: Start with a copy of your program from Exercise 8-9. Write a function called send_messages() 
# that prints each text message and moves each message to a new list called sent_messages as it’s printed. 
# After calling the function, print both of your lists to make sure the messages were moved correctly.

def moved_messages(text_messages, sent_message):
    print("\nMessages are beeing moved")
    """"""
    while text_messages:
        moved_message = text_messages.pop()
        sent_message.append(moved_message)
        

def sent_messages(text_messages):
    """"""
    print("\nMessages are beeing sent")
    
    for text_message in text_messages:
        print(f"{text_message}")



messages = ["hi", "hey", "what you doing?", "nothing", "alr"]
sented_messages = []

moved_messages(messages, sented_messages)
sent_messages(sented_messages)
