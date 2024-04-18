def Prime(y):
    if y < 2:
        return 0
    else:
        x = y // 2
        for i in range(2, x + 1):
            if y % i == 0:
                return 0
    return 1

a = 1
b = 100
for z in range(a, b +1) :
    if Prime(z):
        print(z,end=" ")

