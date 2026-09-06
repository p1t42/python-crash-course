# Three Restaurants: Start with your class from Exercise 9-1. Create three different instances 
# from the class, and call describe_restaurant() for each instance.

class restaurant:
    """a simple attempt to model a restaurant"""
    
    def __init__(self, name, cuisine):
        """initialize name and cuisen atributes"""
        self.name = name
        self.cuisine = cuisine
    
    def describe_restaurant(self):
        """simulate describing a restaurant"""
        print(f"\nThe restaurant is called {self.name} and it make {self.cuisine} food")
        
    def open_restaurant(self):
        """Simulating oppening a restaurant"""
        print(f"\nThe {self.name} restaurant is open")
        


restaurant_1 = restaurant("MacDonalds", "American")
restaurant_2 = restaurant("Dominos", "Italian")
restaurant_3 = restaurant("Lagomandra", "Greek")

restaurant_1.open_restaurant()
restaurant_1.describe_restaurant()
restaurant_2.describe_restaurant()
restaurant_3.describe_restaurant()