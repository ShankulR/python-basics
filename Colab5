company = {
  "name": "Tesla",              # this is called dictionary iteam. This dictionary has 3 items. 
  "founder": 'Elon Musk',
  "established": 2003
}
print(company)

print(company['name'])

print(len(company))

company['name'] = 'TESLAA'
print(company)

print(company.get('name'))   # get() is predefined function for dict 
print(company.get('namee'))  # namee is not defined, so we get None

print(company.keys())
print(company.values())

company['newkey'] = 'newval'
print(company.keys())
print(company.values())

student = {
    'name' : 'John',
    'age' : 12,
    'class' : 7
}
print(student)
student.pop('class')    # use pop function and pass key
print(student)

student = {
    'name' : 'John',
    'age' : 12,
    'class' : 7
}
print(student)
student.clear()
print(student)

new = dict({'name': 'Apple', 'year': 1975, 'founder': 'Steve Jobs and Steve Wozniak'})     # dict is special keyword, wrap your dictionary within dict() 
print(new)
print(type(new))

for item in new:              # this loops over only keys
  print(item)

for item, val in new.items():
  print(item, val)

for key in new.keys():
  print(key)

for xyz in new.values():
  print(xyz)

company = {
    'name': 'Apple',
    'year': 1975,
    'founders': {
        'first': 'Steve Jobs',
        'second': 'Steve Wozniak'
    }
    }
print(company)

for item, val in company.items():
  print(item, val)