# Write a function called make_shirt() that accepts a size and the text of a message that should be 
# printed on the shirt. The function should print a sentence summarizing the size of the shirt and 
# the message printed on it

def make_shirt(size, text):
    print(f"\nThe shirts size is {size} and the text on it is {text}.\n")
    
make_shirt("M", "I like Python")
make_shirt(size="m", text="I love python")