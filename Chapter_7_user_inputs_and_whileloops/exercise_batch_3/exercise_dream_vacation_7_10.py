# 7-10. Dream Vacation: Write a program that polls users about their dream vacation. 
# Write a prompt similar to If you could visit one place in the world, where would you go? 
# Include a block of code that prints the results of the poll.

prompt_1 = "\nWhats Your first name? "
prompt_2 = "\nWhere in the world would you go right now? "
poll = {}

active = True
while active: #if here is any variable asigned the loop checks wheter the variable meets its condition for 
              #example it checks wether active is true, if it would be a list variable it would check wheter 
              # the list is full.
    
    user_name = input(prompt_1)
    user_place = input(prompt_2)
    

    poll[user_name] = user_place    # Adds a key-value pair to the 'poll' dictionary: so in the [] is key and after = is the value
    
    brakes = input("\n Does anyone want to take a poll? (y/n) ")
    if brakes == "y":
        active = False
        
print("\n----Poll End----\n")
for name, place in poll.items():
    print(f"{name} would like to visit {place}\n")