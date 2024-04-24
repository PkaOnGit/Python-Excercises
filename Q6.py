x = int(input('Balance = '))
z = int(input("years deposit = "))
if x > 99999:
    y = x * 1.07

elif 100000 > x >= 50000:
    y = x * 1.05

else: y = x * 1.03

print(f"Balance = {y * z}")

