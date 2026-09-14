# 10-6. Addition: One common problem when prompting for numerical input occurs when people provide 
# text instead of numbers. When you try to convert the input to an int, you’ll get a ValueError.
# Write a program that prompts for two numbers. Add them together and print the result. Catch the 
# ValueError if either input value is not a number, and print a friendly error message. 
# Test your program by entering two numbers and then by entering some text instead of a number.

prompt = "I will take 2 numbers and add them together"

try:
    first_num = input("Enter the first number: ")
    second_num = input("Enter the second number: ")
    output = int(first_num) + int(second_num)
except ValueError:
    print("please provide a number")
else:
    print(output)