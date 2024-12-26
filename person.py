class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        
    
class User:
    def __init__(self, first_name, last_name, age, login_attempts):
        self.person = Person(first_name, last_name)
        self.age = age
        self.login_attempts = login_attempts
        
    def describe_user(self):
        print(f"\nThe user's name is {self.person.first_name} {self.person.last_name}")
        print(f"Age - {self.age}")
        
    def greet_user(self):
        greeting  = self.person.first_name + " " +  self.person.last_name
        print("\nHello", greeting)
        
    def increment_login_attempts(self, num):
        self.login_attempts += num
    
    def print_login_attempts(self):
        print(f"Login attempts: {self.login_attempts}")    
    
    def reset_login_attempts(self):
        self.login_attempts = 0
        
user_1 = User("Ali", "Li", "23", 0)

user_1.describe_user()
user_1.greet_user()
user_1.increment_login_attempts(5)
user_1.print_login_attempts()
user_1.reset_login_attempts()
user_1.print_login_attempts()



