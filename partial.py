from functools import partial

def multiply(a, b):
    return a * b


result = partial(multiply, 2)

print(result(5))

