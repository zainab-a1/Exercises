class Restaurant:   
    """A simple restaurant model"""
    def __init__(self, restaurant_name, cuisine_type, number_served = 0):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = number_served
        
    def describe_restuarant(self):
        """Simulate information about the restaurant in response to a command"""
        print(f"\nThe restaurant is called {self.restaurant_name}.")
        print(f"The type of cuisine is {self.cuisine_type}.")
        
    def open_restuarant(self):
        """Simulate the opening of the restauarnt in response to a command"""
        print(f"The restuarant is now open.") 
    
    def update_served(self, num):
        
        if num >= self.number_served:
            self.number_served = num
        
            
    def increment_num_served(self, num):
        self.number_served = self.number_served + num
    
    def print_num_served(self):
        print(f"The number served is now {self.number_served}")
        
"""Now make three objects(instances)"""

restaurant_1 = Restaurant("Ali", "Thai")

restaurant_1.number_served = 25

restaurant_1.print_num_served()
restaurant_1.describe_restuarant()
restaurant_1.open_restuarant()
restaurant_1.update_served(25)
restaurant_1.increment_num_served(250)
restaurant_1.print_num_served()
