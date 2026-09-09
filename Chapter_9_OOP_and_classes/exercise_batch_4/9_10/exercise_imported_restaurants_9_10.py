# 9-10. Imported Users: Using your latest User class, store it in a module. Make a separate file that 
# imports Users. Make a User instance, and call one of User's methods to show that the import 
# statement is working properly.

from user import User as us
from admin import Admin as ad
from privileges import Privileges

first_user = us("Peter", "fedotovskii", "New York", "Python and Web Development")
second_user = us("John", "Doe", "London", "Data Science")
admin = ad("Martin", "Scott", "San Francisco", "HR department")

first_user.greet_user()
second_user.greet_user()
admin.greet_user()

first_user.show_login_attempts()

admin.privileges.show_privileges()

admin.increment_login_attempts()
admin.increment_login_attempts()

admin.show_login_attempts()
