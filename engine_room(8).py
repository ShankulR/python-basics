a = 33
b = 200
if b > a:
  print("b is greater than a")


n = int(input(" Enter a number to check:"))
if n % 2 == 0:
  print("It's an even number.")
if n % 2 != 0:
  print("It's an odd number.")
if n == 0:
  print("The number is neither even nor odd. Rather you entered Zero.")


a = int(input("Enter the Value of a: "));  
b = int(input("Enter the Value of b: "));  
c = int(input("Enter the Value of c: "));  
if a>b and a>c:  
    print("a is largest input.");  
if b>a and b>c:  
    print("b is largest input.");  
if c>a and c>b:  
    print("c is largest input.");  



a = 200
b = 33
if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")


marks = int(input("Enter the marks? "))  
if marks > 85 and marks <= 100:  
   print("Congrats ! you scored grade A ...")  
elif marks > 60 and marks <= 85:  
   print("You scored grade B + ...")  
elif marks > 40 and marks <= 60:  
   print("You scored grade B ...")  
elif (marks > 30 and marks <= 40):  
   print("You scored grade C ...")  
else:  
   print("Sorry you are fail !!")  
