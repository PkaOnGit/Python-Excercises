def factorial(x):
    if x != 0:
        return (x * (factorial(x-1)))
    else: return 1

try:
    z = int(input("Insert the number: " ))
    if not type(z) is int:
        raise TypeError
    print(factorial(z))
except:
    print("Error")