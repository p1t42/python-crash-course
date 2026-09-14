# 10-13. User Dictionary: The remember_me.py example only stores one piece of information, the username. 
# Expand this example by asking for two more pieces of information about the user, 
# then store all the information you collect in a dictionary. Write this dictionary to a file using json.dumps(), 
# and read it back in using json.loads(). Print a summary showing exactly what your program remembers about the user.

from pathlib import Path
import json

def get_stored_username(path):
    """Get stored username if available."""
    if path.exists():
        contents = path.read_text()
        user_data = json.loads(contents)
        return user_data
    else:
        return None

def get_new_username(path):
    """Prompt for a new username."""
    user_name = input("\nWhat is your name? ")
    fav_food = input("\nWhat is favourite food? ")
    fav_city = input("\nWhat is favourite city? ")
    
    # store the inputs as a dictionary
    user_data = {
        user_name: [fav_food, fav_city],
        }
    contents = json.dumps(user_data)
    path.write_text(contents)
    return user_data

def greet_user():
    """Greet the user by name."""
    path = Path("Chapter_10_files_and_exeptions/json_files/user_data.json")
    user_data = get_stored_username(path)
    #extract keys and values
    if user_data:
        name = list(user_data.keys())[0] 
        info = user_data[name] 
        print(f"Welcome back, {name}!") 
        print(f"Your favorite color is {info[0]}") 
        print(f"Your favorite food is {info[1]}")
    else:
        user_data = get_new_username(path)
        name = list(user_data.keys())[0]
        print(f"We'll remember you, {name}!")

greet_user()
