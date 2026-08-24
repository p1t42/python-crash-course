#  Modify the make_shirt() function so that shirts are large by default with a message that reads I love Python. 
# Make a large shirt and a medium shirt with the default message, and a shirt of any size with a different message.



def make_shirt(size="Large", text="I love python"):
    print(f"\nThe shirts size is {size} and the text on it is {text}.\n")
    
make_shirt()
make_shirt(size="Medium")
make_shirt(size="Small", text="I love coding")