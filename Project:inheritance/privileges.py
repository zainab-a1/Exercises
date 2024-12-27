class Privileges:
    def __init__(self):
        self.privileges = [
            "can add post", "can delete post", "can edit post", "can ban user"
            ]
          
    def show_privileges(self):
        """Display the admin's privileges."""
        print("\nAdmin privileges:")
        for privilege in self.privileges:
            print(f"- {privilege}.")