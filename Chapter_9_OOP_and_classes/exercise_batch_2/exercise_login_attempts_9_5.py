# 9-5. Login Attempts: Add an attribute called login_attempts to your User class from Exercise 9-3 (page 162). 
# Write a method called increment_login_attempts() that increments the value of login_attempts by 1. 
# Write another method called reset_login_attempts() that resets the value of login_attempts to 0.

# Make an instance of the User class and call increment_login_attempts() several times. 
# Print the value of login_attempts to make sure it was incremented properly, and then call
# reset_login_attempts(). Print login_attempts again to make sure it was reset to 0.

class User:
    """attempt to simulate users"""
    
    def __init__(self, first_name, last_name, location, work_field):
        """Initialize user first and last name, location and workfield """
        self.first_name = first_name
        self.last_name = last_name
        self.location = location
        self.work_field = work_field
        self.login_attempts = 0
        
    def describe_user(self):
        """ """
        print(f"\nThis is user {self.first_name.title()} {self.last_name.title()}, who is located in {self.location} and works in {self.work_field}")
    
    def greet_user(self):
        print(f"\nHello {self.first_name.title()} {self.last_name.title()}")
        
    def increment_login_attempts(self):
        self.login_attempts += 1
    
    def reset_login_attempts(self):
        self.login_attempts = 0


user = User("peter", "fedotovskii", "new york", "python development")

user.greet_user()
user.describe_user()

user.increment_login_attempts()
user.increment_login_attempts()

print(f"\nLogin attempts: {user.login_attempts}")

user.reset_login_attempts()
print(f"After reset: {user.login_attempts}")