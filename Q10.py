x = (input("Years = ")) 

try:
    if int(x) % 4 == 0:
        print(f"{x} is a leap year")
    else : 
        print(f"{x} is not a leap year")
except: 
    print("Please type number")