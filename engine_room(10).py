x = 1
while x < 5:        # syntaxt is similar to for or if loop. Starts with while, ends with :, indentation for the while-block
    print(x)
    x += 1       


x = 1
while x < 10:
    if x == 4:
        break
    print(x)
    x += 1


while True:
    name = input('Input name: ')
    if name == 'stop':
        break
    print("Your name is:", name)


i = 0  
str1 = 'Beautiful'    
while i < len(str1):   
    if str1[i] == 't':   
        i += 1  
        break  
    print('Current Letter :', str1[i])   
    i += 1 