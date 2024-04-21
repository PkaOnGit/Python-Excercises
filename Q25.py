def fibonacci(x):
    if x <= 1 :
        return x
    else: return fibonacci(x - 1) + fibonacci(x - 2)


y = int(input("Insert number: "))

print(fibonacci(y))