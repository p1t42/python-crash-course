# 9-8. Privileges: Write a separate Privileges class. The class should have one attribute, privileges, that stores a 
# list of strings as described in Exercise 9-7. Move the show_privileges() method to this class. 
# Make a Privileges instance as an attribute in the Admin class. Create a new instance of Admin and use your 
# method to show its privileges.
        
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
        """Prints a summary of the user's information."""
        print(f"\nThis is user {self.first_name.title()} {self.last_name.title()}, who is located in {self.location} and works in {self.work_field}")
    
    def greet_user(self):
        print(f"\nHello {self.first_name.title()} {self.last_name.title()}")
        
    def increment_login_attempts(self):
        self.login_attempts += 1
    
    def reset_login_attempts(self):
        self.login_attempts = 0
        

class Admin(User):
    """Represents an administrator, a special kind of user with privileges."""
    
    def __init__(self, first_name, last_name, location, work_field):
        """Initialize admin attributes and default privileges."""
        super().__init__(first_name, last_name, location, work_field)
        self.privileges = Privileges()
        
    def greet_user(self):
        """Prints a greeting with the Admin title."""
        print(f"\nHello Admin {self.first_name.title()} {self.last_name.title()}")
    

class Privileges:
    """Stores and manages administrator privileges."""
    
    def __init__(self, privileges=None):
        """Initialize privileges with a default list of admin privileges."""
        privileges = ["can add post", "can delete post", "can ban user", "can edit user", "can view reports"]
        self.privileges = privileges
    
    def show_privileges(self):
        """Lists the administrator's set of privileges."""
        print("\nYour Privileges:")
        for privilege in self.privileges:
            print(f"\t{privilege}")



new_admin = Admin("Peter", "fedotovskii", "New York", "Python and Web Development")

new_admin.greet_user()
new_admin.privileges.show_privileges()

