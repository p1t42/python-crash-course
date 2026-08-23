#Movie Tickets: A movie theater charges different ticket prices depending on a person’s age. 
# If a person is under the age of 3, the ticket is free; if they are between 3 and 12, 
# the ticket is $10; and if they are over age 12, the ticket is $15. Write a loop in 
# which you ask users their age, and then tell them the cost of their movie ticket.



prompt = "\nWrite your actual age: "


while True:
    
    age_input = input(prompt)
    
    persons_age = int(age_input)
    
    if persons_age <= 3:
        price = "free"
    elif persons_age <= 18:
        price = 5
    elif persons_age <= 65:
        price = 10
    else:
        price = "free"
    
    print(f"\nyour movie ticket costs: {price}$")
    break