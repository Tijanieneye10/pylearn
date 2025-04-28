names = ("apple", "mango")
print(type(names))

def user_info():
    name = "John"
    age = 18
    return name, age

person = user_info()
_, age = person
print(f'{age} is showing here')
print(type(person))