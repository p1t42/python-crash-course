# 10-12. Favorite Number Remembered: Combine the two programs you wrote in Exercise 10-11 into one file. If the number 
# is already stored, report the favorite number to the user. If not, prompt for the user’s favorite number and store 
# it in a file. Run the program twice to see that it works.

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
