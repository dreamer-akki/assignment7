# Write a program to display day name on the basis of user’s liking of a colour. Ask
#user for his favorite colour. User can answer in a sentence like “I like red colour”.
#Assuming all colour name entered by user is in lowercase. Use match case to display
#day name associated with the colour.
#a. Yellow - Monday
#b. Blue - Tuesday
#c. Orange - Wednesday
#d. White - Thursday
#e. Black - Friday
#f. Red - Saturday
#g. All other colours - Sunday

col=input("Enter the colour\n")
match col:
    case col if "yellow" in col:
    
            print("Monday")
    case col if "blue" in col:
        print("Tuesday")
    case col if "orange" in col:
        print("Wednesday") 
    case col if "white" in col:
        print("Thusday")
    case col if "black" in col:
        print("Friday")
    case col if "red" in col:
        print("Saturday") 
    case _:
        print("Sunday")                       