# Archived Messages: Start with your work from Exercise 8-10. Call the function send_messages() 
# with a copy of the list of messages. After calling the function, print both of your lists to 
# show that the original list has retained its messages.

def moved_messages(text_messages, sent_message):
    """Move all messages from text_messages to sent_message."""
    print("\nMessages are beeing moved")
    while text_messages:
        moved_message = text_messages.pop()
        sent_message.append(moved_message)
        

def sent_messages(text_messages):
    """Print each message in text_messages."""
    print("\nMessages are beeing sent")
    
    for text_message in text_messages:
        print(f"{text_message}")



messages = ["hi", "hey", "what you doing?", "nothing", "alr"]
sented_messages = []

# we take a copy of the messages variable so the list above is untouched
moved_messages(messages[:], sented_messages)
sent_messages(sented_messages)

print("\nOriginal list:", messages)
print("Sent messages:", sented_messages)

