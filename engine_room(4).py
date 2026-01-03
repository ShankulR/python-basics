courses = ('ba', 'bcom', 'bsc')
print(courses)
print(type(courses))


print(courses[1])

print(courses.count('ba'))
print(courses.count('baa'))

print(courses.index('bsc'))

courses = ('ba', 'bcom', 'bsc', 'bsc', 'ba')
print(courses)
print(courses.count('bsc'))            # 'bsc' is used twice hence 2
print(courses.index('bsc'))            # index returns the index of first occurance (so even if bsc is defined at index 2 and index 3, output will be 2)


for item in courses:     
  print(item)

for id, item in enumerate(courses):    # enumerate() returns index along with main data. Hence you need two variables at the left (id, item). These names could be any. 
  print(id, item)

nums = (2, 3, 4)
print(type(nums))

new = ('50')              # this will be treated as string
print(type(new))
print('-----------------------------')
new1 = ('50',)            # this will be treated as tuple
print(type(new1))

new = ('50',)
new1 = ('apple',)
new2 = ('mango','orange')
print(new + new1 + new2)

print(('a','b','c') + (1, 2, 3))

fruits = ('apple','mango')
print('mango' in fruits)     # return True if 'mango' is part of fruits else False. Thanks to 'IN', it comes handy many times in the real world programs. 
print('mangoes' in fruits)

num = (1, 2, 3, 4, 5, 6, 7)
print(num[-1])
print(num[-2])

courses = ('ba', 'bcom', 'bsc', 'be', 'ma', 'mcom',' msc', 'me')
print(courses[3:5])   # print courses from 3rd index to 5th
print(courses[3:])   # print courses from 3rd index onwards
print(courses[:3])   # print courses upto 3d index