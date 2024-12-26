class Dog:
    """A simple attempt to model a dog."""
    def __init__(self, name , age):
        """Initialise name and age attribute."""
        self.name = name
        self.age = age
        
    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(f"{self.name} is now sitting.")
        
    def roll_over(self):
        """Simulate a dog rolling over in response to a command."""
        print(f"{self.name} is now rolling over.")
        
my_dog = Dog("Willie", 6)
print(f"My dog's name is {my_dog.name}")
print(f"My dog is {my_dog.age} years old")

# Another way to call the function.
my_dog = Dog("Willie", 6)

my_dog.sit()
my_dog.roll_over()