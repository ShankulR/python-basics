courses = ['ba', 'bcom', 'bsc', 'be']
for course in courses:
    print(course)


company = {'name': 'Tesla', 'founder':'Elon', 'year': 2003}
for item in company:
    print(item, company[item])


text = 'Hello'
for i in text:
  print(i)


for i in range(5):   # prints from 0 to 4
  print(i)
print('------------')
for i in range(3,8):   # prints from 3 to 7
  print(i)


courses = ['ba', 'bcom', 'bsc', 'be']
for course in courses:
  if course == 'bsc':
    continue
  print(course)


name = input('enter your name --- ')
print("let's print characeter separately")
for char in name:
  print(char)  


num = [1, 2, 3, 4, 5, 6, 7]
def sqr(item):
  return item * item
for i in num:
  print(i, sqr(i))


num = int(input("Enter the number "))  
for i in range(1,11):  
    c = num * i  
    print(f"{num} x {i} ====> {c}") 


rows = int(input("Enter the rows  :"))    # e.g. 3
for i in range(0, rows+1):               # Outer loop will print number of rows   (+1 because range excludes the second number)
    for j in range(i):                   # Inner loop will print number of Astrisk  
        print("*", end='')               # print() can take different arguments, by default end='\n' i.e. new line
    print()