from user import User
from privileges import Privileges

"""Module for representing administrators."""

class Admin(User):
    """Represents an administrator, a special kind of user with privileges."""
    
    def __init__(self, first_name, last_name, location, work_field):
        """Initialize admin attributes and default privileges."""
        super().__init__(first_name, last_name, location, work_field)
        self.privileges = Privileges()
        
    def greet_user(self):
        """Prints a greeting with the Admin title."""
        print(f"\nHello Admin {self.first_name.title()} {self.last_name.title()}")
    