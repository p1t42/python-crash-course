# 7-9. No Pastrami: Using the list sandwich_orders from Exercise 7-8, make sure the sandwich 'pastrami' 
# appears in the list at least three times. Add code near the beginning of your program to print a message 
# saying the deli has run out of pastrami, and then use a while loop to remove all occurrences of 'pastrami' 
# from sandwich_orders. Make sure no pastrami sandwiches end up in finished_sandwiches.


sandwich_orders = ["Subway", "pastrami", "Grilled Cheese", "pastrami", "Tuna", "pastrami"]
finished_sandwiches =[]

while "pastrami" in sandwich_orders:
    sandwich_orders.remove("pastrami")

print("\nDeli has run out of pastrami")
for sandwich in sandwich_orders:
    print(f"\nYour {sandwich} sandwich has been made")
    
    finished_sandwiches.append(sandwich)

print("\nThese sandwiches were made:")
for finished_sandwich in finished_sandwiches:
    print(f"\t{finished_sandwich} snadwich")
    
    