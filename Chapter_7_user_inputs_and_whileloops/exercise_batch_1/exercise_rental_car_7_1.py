avalible_cars = ["subaru", "toyota", "porshe"]
users_car = input("\nWhat kind of car would you like (only the company's name): ")

if users_car in avalible_cars:
    print("\nThat car is avalible, we will start on the paper work")
else:
    print("\nSorry, this car is taken, would you like a subaru?\n")