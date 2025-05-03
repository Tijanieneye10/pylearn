import typehint
from typehint import fullname

def multiply(x: int, y:int) -> int:
    return x * y

def add(x, y):
    return x + y


print(typehint.fullname("John", "Smith"))
print(fullname("John", "Doe"))