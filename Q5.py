x = int(input("Purchased amount = "))

if x >= 5000:
    Paid = x*0.9
    
elif 5000 > x >= 4000 :
    Paid = x*0.93
    
elif 4000 > x >= 3000 :
    Paid = x*0.95
    
elif 3000 > x >= 2000 :
    Paid = x* 0.97
    
elif x < 2000 :
    Paid = x* 0.98

print(f"Paid= {Paid}")