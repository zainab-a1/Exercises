# main.py

# Import admin and User classes.

from user import User, Admin 

# Creating objects.              
user_1 = User("Ali", "Li", "23", 0)
user_2 = Admin("Lilly", "M", 27, 0)

# User interactions / calling methods.
user_1.describe_user()
user_1.greet_user()
user_1.increment_login_attempts(5)
user_1.print_login_attempts()
user_1.reset_login_attempts()
user_1.print_login_attempts()

# Admin interactions / calling method.
user_2.show_privileges()