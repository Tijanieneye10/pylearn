
def recursive(n):
    if n == 0:
        return 1
    else:
        return n + recursive(n - 1)

print(recursive(5))