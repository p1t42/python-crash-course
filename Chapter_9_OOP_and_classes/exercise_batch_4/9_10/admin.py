from user import User

"""Module for representing administrators."""

class Admin(User):
    """Represents an administrator, a special kind of user with privileges."""
    
    def __init__(self, first_name, last_name, location, work_field, privileges=None):
        """Initialize admin attributes and default privileges."""
        super().__init__(first_name, last_name, location, work_field)
        privileges = ["can add post", "can delete post", "can ban user", "can edit user", "can view reports"]
        self.privileges = privileges
        
    def greet_user(self):
        """Prints a greeting with the Admin title."""
        print(f"\nHello Admin {self.first_name.title()} {self.last_name.title()}")
        
    def show_privileges(self):
        """Lists the administrator's set of privileges."""
        print(f"\nThose are your privileges admin:")
        for privilege in self.privileges:
            print(f"\t{privilege}")
    