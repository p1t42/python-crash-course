prompt = "\nWhat topings would you like on your pizza?"
prompt += "\nenter 'finish' if you done with topings "
prompt += "\n"

active = True
while active:
    topings = input(prompt)
    if topings == "finish":
        active = False
    else:
        print("\nYour topings will be added, anything else")
