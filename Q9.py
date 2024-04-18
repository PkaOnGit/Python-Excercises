x = int(input("Salary = "))

if x >= 40000:
    y = x * 0.8
elif 20000 <= x < 40000:
    y = x * 0.85
elif 10000 <= x < 20000:
    y = x* 0.9
elif x < 10000 :
    y = x * 1

print(f"Net Salary is {y}")