names = ("apple", "mango")
print(type(names))

def user_info():
    name = "John"
    age = 18
    return name, age

person = user_info()
name, age = person
print(name, age)
print(type(person))