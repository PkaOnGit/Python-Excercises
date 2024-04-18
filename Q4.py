x = int(input("Purchased amount = "))

if x >= 1000:
    Paid = x*0.95
   
else:
    Paid = x*0.97

print(f"Paid= {Paid}")