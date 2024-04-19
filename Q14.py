def digitsum(x):
    sum = 0
    for i in str(x):
        sum += int(i)
    return sum

x = str(input("Number: "))

print(f"Sum of the digits = {digitsum(x)}")



