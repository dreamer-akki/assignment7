#Write a menu driven program to perform following operations - Addition, Subtraction,Multiplication, Division

a= input("Enter the operater \n")
match a:
    case "+":
        n1= int(input("Enter the 1st number,it should be greater the 2nd number \n"))
        n2=int(input("Enter the 2nd number\n"))
        print("Addition is:",n1+n2)
    case "-":
         n1= int(input("Enter the 1st number,it should be greater the 2nd number \n"))
         n2=int(input("Enter the 2nd number\n"))
         print("Substraction is:",n1-n2)
    case "*":
        n1= int(input("Enter the 1st number,it should be greater the 2nd number \n"))
        n2=int(input("Enter the 2nd number\n"))
        print("Multiplication is:",n1*n2)
    case "/":
        n1= int(input("Enter the 1st number,it should be greater the 2nd number \n"))
        n2=int(input("Enter the 2nd number\n"))
        print("Division is:",n1/n2)    
    case _:
        print("Enter a valid operator")
