# 9-4. Number Served: Start with your program from Exercise 9-1 (page 162). Add an attribute called 
# number_served with a default value of 0. Create an instance called restaurant from this class. 
# Print the number of customers the restaurant has served, and then change this value and print it again.

# Add a method called set_number_served() that lets you set the number of customers that have been served. 
# Call this method with a new number and print the value again.

# Add a method called increment_number_served() that lets you increment the number of customers who’ve been served. 
# Call this method with any number you like that could represent how many customers were served in, say, a day of business.


class restaurant:
    """a simple attempt to model a restaurant"""
    
    def __init__(self, name, cuisine):
        """initialize name and cuisen atributes"""
        self.name = name
        self.cuisine = cuisine
        self.number_served = 0
    
    def describe_restaurant(self):
        """simulate describing a restaurant"""
        print(f"\nThe restaurant is called {self.name} times")
        print(f"\nThe restaurant is making {self.cuisine} food")
        
    def open_restaurant(self):
        """Simulating oppening a restaurant"""
        print(f"\nThe {self.name} restaurant is open")

    def served_number(self):
        print(f"The restaurant has served {self.number_served}")
    
    def set_number_served(self, new_served_number):
        """changing the nember_served"""
        self.number_served = new_served_number        
    
    def increment_number_served(self, incremented_number):
        self.number_served += incremented_number
        

restaurant_1 = restaurant("Chicki", "Russian")

restaurant_1.describe_restaurant()
restaurant_1.set_number_served(23)
restaurant_1.served_number()
restaurant_1.increment_number_served(10)
restaurant_1.served_number()
