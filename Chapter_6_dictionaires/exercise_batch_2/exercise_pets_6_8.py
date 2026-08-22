# Make several dictionaries, where each dictionary represents a different pet. 
# In each dictionary, include the kind of animal and the owner’s name. 
# Store these dictionaries in a list called pets. Next, loop through your list 
# and as you do, print everything you know about each pet.

pet_0 = {"kind": "cat",
         "owner": "pit",
         }    

pet_1 = {"kind": "dog",
         "owner": "vlad",
         } 

pet_2 = {"kind": "hamster",
         "owner": "roma",
         } 

pets = [pet_0, pet_1, pet_2]

for pet in pets:
        pet_kind = pet["kind"]
        pet_owner = pet["owner"]
        
        print(f"\n This is a {pet_kind} and the owner's name is {pet_owner}")