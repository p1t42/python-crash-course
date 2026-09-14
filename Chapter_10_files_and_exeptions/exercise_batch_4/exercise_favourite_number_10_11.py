# 10-11. Favorite Number: Write a program that prompts for the user’s favorite number. Use json.dumps() 
# to store this number in a file. Write a separate program that reads in this value and prints the message 
# “I know your favorite number! It’s _____.”

from pathlib import Path
import json

path = Path("Chapter_10_files_and_exeptions/json_files/fav_num.json")

if path.exists():
    contents = path.read_text()
    fav_num = json.loads(contents)
    print(f"Your favourite number is {fav_num}")
else:
    fav_num = input("\nWhat's your favourite number? ")
    fav_num = int(fav_num)
    contents = json.dumps(fav_num)
    path.write_text(contents)
    print(f"\nWe'll remember your favourite number when you come back, {fav_num}!")
