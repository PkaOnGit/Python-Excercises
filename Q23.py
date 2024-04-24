def sumoftwo(x,y):
    return x + y
try:
    num1 = int(input("First number: "))
    num2 = int(input("Second number: "))

    if not type(num1 and num2) is int:
        raise TypeError

#sum = sumoftwo(num1,num2)

    print(f"this is the sum of two number {sumoftwo(num1,num2)}")
except:
    print("Error")