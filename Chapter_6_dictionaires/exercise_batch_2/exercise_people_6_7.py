jen = {"Firstname": "jen",
       "Lastname": "swanson",
       "food": "chips",
       "hobby": "working with clay",
       }

roma = {"Firstname": "roman",
        "Lastname": "fedtovskii",
        "food": "govna",
        "hobby": "football",
        }

peter = {"Firstname": "peter",
         "Lastname": "peterson",
         "food": "fries",
         "hobby": "coding",
         }

people = [jen, roma, peter]

for person in people:
    print(f"\nPerson's name: {person['Firstname']}")
    print(f"\t{person['Firstname']}'s fullname is {person['Firstname']} {person['Lastname']}")
    print(f"\t{person['Firstname']}'s favourite food is {person['food']}")
    print(f"\t{person['Firstname']}'s hobby is {person['hobby']}")

# cwe could theoreticle put another for loop and make it like this:
# for key, value in person.items():