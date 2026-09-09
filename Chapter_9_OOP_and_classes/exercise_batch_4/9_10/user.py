"""Module for representing users."""

class User:
    """Represents a user with a name, location, work field, and login tracking."""
    
    def __init__(self, first_name, last_name, location, work_field):
        """Initialize user first and last name, location and workfield """
        self.first_name = first_name
        self.last_name = last_name
        self.location = location
        self.work_field = work_field
        self.login_attempts = 1
        
    def describe_user(self):
        """Prints a summary of the user's information."""
        print(f"\nThis is user {self.first_name.title()} {self.last_name.title()}, who is located in {self.location} and works in {self.work_field}")
    
    def greet_user(self):
        """Prints a personalized greeting."""
        print(f"\nHello {self.first_name.title()} {self.last_name.title()}")
        
    def show_login_attempts(self):
        """ """
        if self.login_attempts == 1:
            print(f"\nThe user {self.first_name.title()} {self.last_name.title()} has {self.login_attempts} login attempt")
        else:
            print(f"\nThe user {self.first_name.title()} {self.last_name.title()} has {self.login_attempts} login attempts")

    def increment_login_attempts(self):
        """Increments the login attempt counter by one."""
        self.login_attempts += 1 

    def reset_login_attempts(self):
        """Resets the login attempt counter to zero."""
        self.login_attempts = 0
        
    

