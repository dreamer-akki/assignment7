#. Write a program which takes user’s age and display the category of person. Age below 10 years- Kid, Age below 20 - Teen, Age below 40 - young, Age below 60 -Experienced, Age above or equal 60 - Senior Citizen

age=int(input("Enter the Age \n"))

match age:
    case age if age<=10:
        if age<=10:
            print("You are Kid")
    case age if age<=20:        
        if age<=20:
            print("You are Teen")
    case age  if age<=40:
        if age<=40:
            print("You are Young") 
    case age if age<=60:
        if age<=60:
            print("You are Experienced")
    case age if age>=60:
        if age>=60:
            print("You are Senior Citizen")
    case _:
        print("Please enter valid age")                       