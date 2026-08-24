# Custom exercise to add input to identify sandwich orders

prompt_1 = "\nWhat sandiwch would you like to order? "
prompt_2 = "\nAnything else (y/n)? "
sandwich_orders = []
finished_sandwiches =[]

print("\nDeli has run out of pastrami")

# while loop to pick up user input or end the picking up
active = True
while active:
    
    user_sandwiches = input(prompt_1)
    sandwich_orders.append(user_sandwiches)
    
    if user_sandwiches == "pastrami":
        print("Sorry but we've run out of pastrami")
    
    breaks = input(prompt_2)
    
    if breaks == "n":
        active = False
        

# while loop that removeces "pastrami" from sandwich_oders 
while "pastrami" in sandwich_orders:
    sandwich_orders.remove("pastrami")


# appending sandwiches to finished_sandwiches + removing all sendwiches from sandwich_order
while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print(f"\nYour {sandwich} sandwich has been made")
    finished_sandwiches.append(sandwich)


# Listing all made sandwiches
print("\nThese sandwiches were made:")
for finished_sandwich in finished_sandwiches:
    print(f"\t{finished_sandwich} snadwich") 
    