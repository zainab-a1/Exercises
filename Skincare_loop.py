print("\nWelcome to Skincare recommendations!\n")
enter = int(input("Enter 1 - start or 2 - stop: "))
while enter == 1:
    skin= input("\nWould you like a tailored skincare routine - Yes / No: ").lower()
    if skin == "yes":
        print("\nGreat! let's take some informaton about the type of your skin.")
        type_of_skin= input("\nIs your skin Dry / Combination or Oily: ").lower()
        if type_of_skin == "dry":
            print("\nUse a gentle wash like an Aleo vera gel.")
        elif type_of_skin == "combination":
            print("\nUse a Qasil based cleanser for your face.")
        elif type_of_skin == "oily":
            print("\nUse a Tea Tree oil based cleanser.")
        cream= input("\nWould you like me to recommed a moistriser for your face - yes or no: ").lower()
        if cream == "yes":
            print("\nElemis pro collagen day cream with 15 SPF.")
        elif cream == "no":
            mask = input("\nNo problem, how about a mask - Yes / No: ")
            if mask == "yes":
                print("\nVitamin E mask would be handy! ")
            elif mask == "no":
                exfoliater = input("\nAnd would like to also add an exfolaiter to your routine - Yes / No: ").lower()
                if exfoliater == "yes":
                    print("\nRice exfoliater with a hydrating mask like Vitamin E mask. ")
                else:
                    print("\nIt's not really a must for skincare routine! ")
        serum= input("\nWould you like to add serums to your routine - Yes or No: ")
        if serum == "yes":
            age= int(input("\nPlease enter your age as serums are best tailered according to your age: "))
            if age <25:
                print("\nUse a Hylaronic acid serum for optimall hydration. ")
            elif age > 25 and age < 45:
                print("\nUse a Retinol active serums, best organic ones would be bukachiol based serums. ") 
            else:
                print("\nUse Collagen and Retinol serums.")
        else:
            spf= input("\nSince you are using actives, it's best to add sunscream, would you like me to recommend one for you - Yes/ No: ").lower()
            if spf == "yes":
                print("\nUse La Roche Posay sunscream. ")
            else:
                print("\nNo problem!")
    else:
        print("\nNo problem, take care of skin! ")
    enter = int(input(" 1 - start or 2 - stop: "))
print("\nEnjoy your day!")
  