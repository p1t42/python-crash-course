# 10-4. Guest: Write a program that prompts the user for their name. When they respond, 
# write their name to a file called guest.txt 

from pathlib import Path

path = Path("/Users/peterfedotovskii/Documents/python_crash_course/Chapter_10_files_and_exeptions/txt_files/dataset_10_4.txt")

user_name = input("\nTell me your name: ")
user_hobby = input("\nTell me your hobby: ")

with path.open("a") as file:
    file.write(f"{user_name}: {user_hobby}\n")
print("Your answears have been saved in our Dataset")