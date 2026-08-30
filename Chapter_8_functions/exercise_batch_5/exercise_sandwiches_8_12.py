# Sandwiches: Write a function that accepts a list of items a person wants on a sandwich. 
# The function should have one parameter that collects as many items as the function 
# call provides, and it should print a summary of the sandwich that’s being ordered. 
# Call the function two times, using a different number of arguments each time.

def print_sanwiches(*sanwiches):
    print("\nHere is your orderd sandwiches")
    for sandwich in sanwiches:
        print(f" - {sandwich}")



ordered_sandwiches = ["tuna sandwich", "my sandwich", "club sandwich", "grilled cheese"]

print_sanwiches(*ordered_sandwiches) #must include * in a call when working with a list.
print_sanwiches("small sandwich", "big sandwich")
