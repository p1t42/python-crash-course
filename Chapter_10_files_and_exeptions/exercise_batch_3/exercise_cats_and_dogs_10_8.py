# 10-8. Cats and Dogs: Make two files, cats.txt and dogs.txt. Store at least three names of cats 
# in the first file and three names of dogs in the second file. Write a program that tries to read 
# these files and print the contents of the file to the screen. Wrap your code in a try-except 
# block to catch the FileNotFoundError, and print a friendly message if a file is missing.
# Move one of the files to a different location on your system, and make sure the code in the 
# except block executes properly.

from pathlib import Path

filenames = ["Chapter_10_files_and_exeptions/txt_files/cats.txt", "Chapter_10_files_and_exeptions/txt_files/dogs.txt"]

# the problem was that the loop was in the the try block which is wrong becouse the loop goes through all of the items and 
# if one is missing the whole loop breaks

# the bug before was that the whole try block was outside the for loop so the whole programm run on the leftover of path asigned to dogs

for filename in filenames:
        path = Path(filename)

        try:
            contents = path.read_text()
        except FileNotFoundError:
            print("The File doesn't exist")
        else:
            print(contents)
    