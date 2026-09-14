# 10-7. Addition Calculator: Wrap your code from Exercise 10-6 in a while loop so the user can continue 
# entering numbers, even if they make a mistake and enter text instead of a number.

prompt_1 = "\nI will take 2 numbers and add them together"
prompt_2 = "Press q if you want to quit"

while True:
    try:  
        print(prompt_1)
        print(prompt_2)
        first_num = input("\nEnter the first number: ")
        if first_num == "q":
            break
        second_num = input("Enter the second number: ")
        if second_num == "q":
            break
        output = int(first_num) + int(second_num)
    except ValueError:
        print("please provide a number")
    else:
        print(output)