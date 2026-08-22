cities = {
    "London": {"country": "England", "population": "20mil", "fact": "has big ben"},
    "Barcelona": {"country": "Spain", "population": "15mil", "fact": "has beautiful streets"},
    "Stuttgart": {"country": "Germany", "population": "4mil", "fact": "has a lot of car museums"},
}

for city, info in cities.items():
    print (f"\nThe city's name is {city}")
    country = info["country"]
    population = info["population"]
    fact = info["fact"]
    
    print(f"It's located in {country}, it has {population} people and {fact}")