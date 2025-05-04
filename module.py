# import typehint
# from typehint import fullname
# import requests
#
# def multiply(x: int, y:int) -> int:
#     return x * y
#
# def add(x, y):
#     return x + y
#
#
# print(typehint.fullname("John", "Smith"))
# print(fullname("John", "Doe"))

import requests

response = requests.get("http://jsonplaceholder.typicode.com/todos/1")

print(response.json())