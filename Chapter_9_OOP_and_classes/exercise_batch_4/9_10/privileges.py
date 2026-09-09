"""Module for managing administrator privileges."""

class Privileges:
    """Stores and manages administrator privileges."""
    
    def __init__(self, privileges=None):
        """Initialize privileges with a default list of admin privileges."""
        privileges = ["can add post", "can delete post", "can ban user", "can edit user", "can view reports"]
        self.privileges = privileges
    
    def show_privileges(self):
        """Lists the administrator's set of privileges."""
        print(f"\nThose are your privileges admin:")
        for privilege in self.privileges:
            print(f"\t{privilege}")