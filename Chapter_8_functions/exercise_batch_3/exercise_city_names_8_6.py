# City Names: Write a function called city_country() that takes in the name of a city and its country. 
# The function should return a string formatted like this: "Santiago, Chile"
# Call your function with at least three city-country pairs, and print the values that are returned.

def city_country(city, country):
    destination = f"{city.title()} {country.title()}"
    return destination

first_destination = city_country("kansas", "USA")
second_destination = city_country("rom", "italy")
third_destination = city_country("berlin", "germany")

print(first_destination)
print(second_destination)
print(third_destination)