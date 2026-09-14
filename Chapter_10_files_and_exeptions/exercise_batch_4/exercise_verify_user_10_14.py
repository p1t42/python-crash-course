# 10-14. Verify User: The final listing for remember_me.py assumes either that the user has already entered their 
# username or that the program is running for the first time. We should modify it in case the current user is not 
# the person who last used the program.

# Before printing a welcome back message in greet_user(), ask the user if this is the correct username. 
# If it’s not, call get_new_username() to get the correct username

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
    #appending new data 
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
        user_input = input(f"Hi, is this the right name: {name}? (y/n) ")
        if user_input != "y":
            get_new_username(path)
        else:
            print(f"Welcome back, {name}!") 
            print(f"Your favorite color is {info[0]}") 
            print(f"Your favorite food is {info[1]}")
    else:
        user_data = get_new_username(path)
        name = list(user_data.keys())[0]
        print(f"We'll remember you, {name}!")

greet_user()
