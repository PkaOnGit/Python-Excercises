try:
    x = int(input("Number: "))
    Order= len(str(x))
    sum = 0

    y = x
    while y > 0:
        Digit = y % 10
        sum += Digit ** Order
        y //= 10

    if x == sum : 
        print(f"{x} is an armstrong number")
    else: print(f"{x} is not an armstrong number")
except:
    print("Error")    
