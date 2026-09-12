# 10-5. Guest Book: Write a while loop that prompts users for their name. Collect all the names that are entered, 
# and then write these names to a file called guest_book.txt. Make sure each entry appears on a new line in the file.

from pathlib import Path

path = Path("/Users/peterfedotovskii/Documents/python_crash_course/Chapter_10_files_and_exeptions/txt_files/dataset_10_5.txt")

while True:
    print("\nWe will collect your data")
    user_input = input("Do you want to proceed? (y/n) ")
    if user_input.lower() != "y":
        print("\nQuiting...")
        break
    
    user_name = input("\nTell me your name: ")
    user_hobby = input("\nTell me your hobby: ")
    
    with path.open("a") as file:
        file.write(f"{user_name}: {user_hobby}\n")
    print("Your answears have been saved in our Dataset")
    

