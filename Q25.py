def fibonacci(x):
    if x <= 1 :
        return x
    else: return fibonacci(x - 1) + fibonacci(x - 2)

try:
    y = int(input("Insert number: "))
    if not type(y) is int:
        raise TypeError
    print(fibonacci(y))
except:
    print("Error")