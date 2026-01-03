num1 = 3
num2 = 5
print(num1, num2)
print(type(num1), type(num2))

print(num1 + num2)
print(num1 - num2)
print(num1 * num2)
print(num2 / num1)   # division sometimes may result in float


print(num2 // num1)  # this is called floor division i.e. the output is quotient without reminder i.e. discarding the numbers after decimal point
print(num2 % num1)   # this is called modulus i.e. the reminder after division
print(3 ** 2)        # exponent (^) ---> 3^2


print(9 % 3)
print(8 % 3)
print(7 % 3)
print(6 % 3)

print(2 == 2)   # if LHS = RHS, output True else False
print(2 == 1)   # Here LHS is not equal to RHS


print(3 != 2)
print(3 > 2)
print(3 < 2)
print(3 >= 3)
print(3 >= 2)
print(3 <= 2)


num = 4
print(num)

num += 1   # is equivalent to num = num + 1
print(num) 


print(True and True)
print(True and False)   # same as False and True
print(False & False)    # instead of and, you can use &
# In short, if any one is false then answer is false 


height = 176
if height < 140:
    print('too short')
elif height < 180:
    print('height is ok')
else:
    print('too tall')


is_subscribed = False
if is_subscribed:              # Read it like - if True do THIS else do THAT
    print('Thank you for the subscription!')  
else:
    print('Please subscribe')


x = 7
if x > 10:
    print('x is greater than 10')
    if x > 20:
        print('x is greater than 20')
        if x > 30:
            print('x is greater than 30')
        else:
            print('x is smaller than 30')
    else:
        print('x is smaller than 20')
else:
    print('x is smaller than 10')
