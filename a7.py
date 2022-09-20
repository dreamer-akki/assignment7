# Write a python program to check whether a given number is positive, negative or
#zero using match case 

num=int(input("enter the number\n"))
match num:
    case num if num>0:
          print("number is positive ")
    case num if num<0:
        print("number is negative")
    case num if num==0:
        print("number is zero")    
    
