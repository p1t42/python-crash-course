# Users: Make a class called User. Create two attributes called first_name and last_name, and then create 
# several other attributes that are typically stored in a user profile. Make a method called describe_user() 
# that prints a summary of the user’s information. Make another method called greet_user() that prints a 
# personalized greeting to the user.

class users:
    """attempt to simulate users"""
    
    def __init__(self, first_name, last_name, location, work_field):
        """Initialize user first and last name, location and workfield """
        self.first_name = first_name
        self.last_name = last_name
        self.location = location
        self.work_field = work_field
        
    def describe_user(self):
        """ """
        print(f"\nThis is user {self.first_name.title()} {self.last_name.title()}, who is located in {self.location} and works in {self.work_field}")
    
    def greet_user(self):
        print(f"\nHello {self.first_name.title()} {self.last_name.title()}")
        
user = users("peter", "fedotovskii", "new york", "python developer")

user.greet_user()
user.describe_user()