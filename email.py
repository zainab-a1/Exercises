### --- OOP Email Simulator --- ###

# --- Email Class --- #
# Create the class, constructor and methods to create a new Email object.

class Email():
        # Declare the class variable, with default value, for emails. 
        has_been_read = False
        
        # Initialise the instance variables for emails.
        def __init__(self, email_address, subject_line, email_content):
            self.email_address = email_address
            self.subject_line = subject_line
            self.email_content = email_content
            
            # Create the method to change 'has_been_read' emails from False to True.
        def edit_values(self):
            self.has_been_read = True
                
 # --- Lists --- #
# # Initialise an empty list to store the email objects.       
inbox = list()

def populate_inbox(): 
    email_1 = Email("data@gmail.com", "English", "Paragraph")
    email_2 = Email("hashtag@live.nl", "Maths", "Exercise questions")
    email_3 = Email("none@icloud.com", "Python", "Language")
 
    inbox.append(email_1)
    inbox.append(email_2)
    inbox.append(email_3)
            
# Create 3 sample emails and add it to the Inbox list. 



# --- Functions --- #
# Build out the required functions for your program. 
    
# call the function to populate inbox
# Create a function which prints the email’s subject_line, along with a corresponding number.


def list_emails():
    for i in range(len(inbox)):
        print(i, inbox[i].subject_line)
    
    
populate_inbox()
list_emails()
    
    
def read_email(index):
    email = inbox[index]
    email.edit_values()
    print("Reading email: ")
    print(email.email_address, email.subject_line, email.email_content )


    

#     # Create a function which displays a selected email. 
#     # Once displayed, call the class method to set its 'has_been_read' variable to True.

# # --- Email Program --- #

# # Call the function to populate the Inbox for further use in your program.

# # Fill in the logic for the various menu operations.
# menu = True

while True:
    user_choice = int(input('''\nWould you like to:
    1. Read an email
    2. View unread emails
    3. Quit application

    Enter selection: '''))
       
    if user_choice == 1:
        choice = int(input(" Would you like to read the first email, second or third email: "))
        if choice == 0:
            print("Invalid choice")
        else:
            read_email(choice-1)
        
    #     # add logic here to read an email
        
    elif user_choice == 2:
        for email in inbox:
            if email.has_been_read == False:
                print(email.email_address, email.subject_line, email.email_content)
    #     # add logic here to view unread emails
            
    elif user_choice == 3:
        exit()
    #     # add logic here to quit appplication

    else:
        print("Oops - incorrecr input.")
    

