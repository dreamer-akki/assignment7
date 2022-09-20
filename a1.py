#1. Write a python script to display the number of days in a given month number.

mon=int(input("Enter the month in numeric format\n"))
match mon:
    case 1:
     print("January has 31 days")
    case 2:
     print("Febuary has 28 or 29 days") 
    case 3:
     print("March has 31 days") 
    case 4:
     print("April has 30 days") 
    case 5:
     print("May has 31 days") 
    case 6:
     print("June has 30 days") 
    case 7:
     print("July has 31 days") 
    case 8:
     print("August has 31 days")     
    case 9:
     print("September has 30 days")   
    case 10:
     print("October has 31 days") 
    case 11:
     print("November has 30 days")                                        
    case 12:
     print("December has 31 days")   
    case _:
     print("Enter a valid month")    
 


