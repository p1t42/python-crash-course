# 8-9. Messages: Make a list containing a series of short text messages. Pass the list 
# to a function called show_messages(), which prints each text message.

def show_messages(text_messages):
    """Print each text message from the list."""
    for text_message in text_messages:
        print(f"{text_message}")

messages = ["hi", "hey", "what you doing?", "nothing", "alr"]
show_messages(messages)
