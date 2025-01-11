print(" Welcome to trip planner 101")
enter = int(input(" 1 - start or 2 - stop: "))
while enter == 1:
    destination= input("Do you have a destinationn in mind? ").lower()
    if destination == "yes":
        print("let's plan your trip")
        transport= input("Plane/Train or Car: ").lower()
        if transport == "plane":
            class_type= input("which fare would you like? (First/Business/Economy): ").lower()
            luggage= int(input("Enter baggage weight in KG: "))
            if luggage >= 21 and class_type == "business" or class_type =="first":
                print("Great, you can have more baggage with these classes")
            elif luggage < 21 and class_type == "business" or class_type == "first":
                print("You can bring more if you want!")
            else:
                print("Warning, you may have too much!")
        elif transport == "train":
            seat_class = input("Economy or business: ").lower()
            if seat_class =='business':
                print("Great! More comfort your way.")
            elif seat_class == "economy":
                print("You save more this way!")
            else:
                print("We don't have that class.")
        elif transport == "car":
            print("Road trips are fun!")
            num_people = int(input("How many people: "))
            if num_people <= 4:
                print("Great, you could rent a car!")
            else:
                print("You may want to rent a van or mini bus!")
        else:
            print("We don't have that transport type ....")
    else:
        print("I can help you choose a destination!")  
        trip_type = input("Beach/City/Adventure: ").lower()
        if trip_type == "beach":
            print("How about Hawaii?")
            beach_type= input("Popular or remote beach ").lower()
            if beach_type == "popular":
                print("check out Waikiki beach")
            elif beach_type == "remote":
                print(" Head over to Maui")
            else:
                print(" We don't have that option...")
        elif trip_type == "city":
            print("Head to New York City")
            activity= input("Indoor or Outdoor? ").lower()
            if activity == "indoor":
                print("check out the Met Museum")
            elif activity == "outdoor":
                print("Relax in Central Park")
            else:
                print("Wrong input, spelling error!")
        elif trip_type == "adventure":
            print("Head out to National park")
            outdoor_activity= input("Hiking or Camping? ").lower()
            if outdoor_activity == "hiking":
                print("Try hiking half Dome")
            elif outdoor_activity == "camping":
                print("check out one of the many camping sites within the park")
            else:
                print("That activiy is not offered")
        else:
            print("That trip is not available")
            
print("Enter for  achance to win a free trip!")
answer= input("What is the largest desert in the world? ").lower()
if answer == "antartica":
    print("Wow, you got a FREE trip!")
else:
    print("Wrong answer, try again!")
    answer=input("What is the largest desert in the world? ").lower()
        
    enter = int(input (" 1 - start or 2 - stop"))
print("Enjoy your trip!")               
                  
                
                
            
            
