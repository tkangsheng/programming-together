def factorial(n):
    if (n == 1):
        return 1
    else:
        return n * factorial(n - 1)

def multiply(a, b):
    return a*b

print(factorial(5))
print(multiply(2, 3))