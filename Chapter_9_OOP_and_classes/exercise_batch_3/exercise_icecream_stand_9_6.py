# Ice Cream Stand: An ice cream stand is a specific kind of restaurant. Write a class called IceCreamStand that 
# inherits from the Restaurant class you wrote in Exercise 9-1 (page 162) or Exercise 9-4 (page 166). 
# Either version of the class will work; just pick the one you like better. Add an attribute called flavors 
# that stores a list of ice cream flavors. Write a method that displays these flavors. Create an instance of 
# IceCreamStand, and call this method.

class Restaurant:
    """a simple attempt to model a restaurant"""
    
    def __init__(self, name, cuisine):
        """initialize name and cuisen atributes"""
        self.name = name
        self.cuisine = cuisine
        self.number_served = 0
    
    def describe_restaurant(self):
        """simulate describing a restaurant"""
        print(f"\nThe restaurant is called {self.name} and it make {self.cuisine} food")
       
    def open_restaurant(self):
        """Simulating oppening a restaurant"""
        print(f"\nThe {self.name} restaurant is open")

    def served_number(self):
        """Display the number of customers served"""
        print(f"The restaurant has served {self.number_served}")
    
    def set_number_served(self, new_served_number):
        """changing the number_served"""
        self.number_served = new_served_number        
    
    def increment_number_served(self, incremented_number):
        """Increment the number served by the given amount"""
        self.number_served += incremented_number


class IceCreamStand(Restaurant):
    """Attempt to model detailed ice creaam restaurant with inheritence from Restaurant"""
    
    def __init__(self, name, cuisine):
        """initialize restaurant's attributes"""
        super().__init__(name, cuisine)
        self.flavors = ["Chocolatte", "Vanille", "Strawberry", "Melon", "Watermelon"]
        
    def diplay_flavors(self):
        """Display all available ice cream flavors"""
        print("\nAvailible Flavors:")
        for flavor in self.flavors:
            print(f"\t{flavor.title()} flavor")

new_restaurant = IceCreamStand("Marco's Ice", "Italian")

new_restaurant.describe_restaurant()
new_restaurant.diplay_flavors()