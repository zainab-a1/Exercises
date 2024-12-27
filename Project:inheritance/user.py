# user.py

from privileges import Privileges

class User:
    def __init__(self, first_name, last_name, age, login_attempts):
        """Initialise user attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.login_attempts = login_attempts
        
    def describe_user(self):
        """Display a summary of the users's information."""
        print(f"\nThe user's name is {self.first_name} {self.last_name}")
        print(f"Age: {self.age}")
        
    def greet_user(self):
        """Display a grreting message to the user."""
        print(f"\nHello {self.first_name} {self.last_name}")
        
    def increment_login_attempts(self, num):
        """Increment the number of login attempts."""
        self.login_attempts += num
    
    def print_login_attempts(self):
        print(f"Login attempts: {self.login_attempts}")    
    
    def reset_login_attempts(self):
        """Display the current number of login attempts."""
        self.login_attempts = 0
 
 
            
class Admin(User):
    def __init__(self, first_name, last_name, age, login_attempts):
        """Initialise an admin user with privileges."""
        super().__init__(first_name, last_name, age, login_attempts)
        self.privileges = Privileges()
    
    def show_privileges(self):
        """Delegate privilage display to the privilage instance."""
        self.privileges.show_privileges()
    