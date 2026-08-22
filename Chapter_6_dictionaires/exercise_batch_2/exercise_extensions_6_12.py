# We’re now working with examples that are complex enough that they can be extended 
# in any number of ways. Use one of the example programs from this chapter, 
# and extend it by adding new keys and values, changing the context of the program, 
# or improving the formatting of the output.

cities = {
    "London": {"country": "England", "population": "20mil", "fact": "has big ben"},
    "Barcelona": {"country": "Spain", "population": "15mil", "fact": "has beautiful streets"},
    "Stuttgart": {"country": "Germany", "population": "4mil", "fact": "has a lot of car museums"},
}

print(f"\n----TRAVEL GUIDE----")

for city, info in cities.items():
    print (f"\nThe city's name is {city.title()}")
    country = info["country"]
    population = info["population"]
    fact = info["fact"]
    
    print(f"It's located in {country.title()}, it has {population} people and {fact}")
    
#imroved: add title(), also added travel guide