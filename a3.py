# Write a menu driven program with the following options:
#a. Check whether a given set of three numbers are lengths of an isosceles triangle or not
#b. Check whether a given set of three numbers are lengths of sides of a right angled triangle or not
#c. Check whether a given set of three numbers are equilateral triangle or not
#d. Exit.

tri=input("Enter a,b,c\n")
match tri:
    case "a":
      s1=int(input("Enter the 1st side of triange\n"))
      s2=int(input("Enter the 2nd side of triange\n"))
      s3=int(input("Enter the 3rd side of triange\n"))
      if s1==s2 or s1==s3 or s2==s3:
        print("Triangle is isosceles")
    case "b":
      s1=int(input("Enter the 1st side of triange\n"))
      s2=int(input("Enter the 2nd side of triange\n"))
      s3=int(input("Enter the 3rd side of triange\n"))
      if s1**s1==s2**s2+s3**s3 or s2**s2==s1**s1+s3**s3 or s3**s3==s1**s1+s2**s2:
        print("Triangle is right angle")
    case "c":
      s1=int(input("Enter the 1st side of triange\n"))
      s2=int(input("Enter the 2nd side of triange\n"))
      s3=int(input("Enter the 3rd side of triange\n"))
      if s1==s2==s3:
        print("Triangle is equilateral")
    case _:
        exit