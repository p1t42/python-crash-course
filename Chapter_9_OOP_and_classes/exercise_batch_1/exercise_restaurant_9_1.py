# Make a class called Restaurant. The __init__() method for Restaurant should store two attributes: 
# a restaurant_name and a cuisine_type. Make a method called describe_restaurant() that prints 
# these two pieces of information, and a method called open_restaurant() that prints a message 
# indicating that the restaurant is open.

class restaurant:
    """a simple attempt to model a restaurant"""
    
    def __init__(self, name, cuisine):
        """initialize name and cuisen atributes"""
        self.name = name
        self.cuisine = cuisine
    
    def describe_restaurant(self):
        """simulate describing a restaurant"""
        print(f"\nThe restaurant is called {self.name}")
        print(f"\nThe restaurant is making {self.cuisine} food")
        
    def open_restaurant(self):
        """Simulating oppening a restaurant"""
        print(f"\nThe {self.name} restaurant is open")
        

restaurant_1 = restaurant("Chicki", "Russian")

restaurant_1.describe_restaurant()
restaurant_1.open_restaurant()