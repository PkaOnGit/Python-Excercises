x = str(input("Numbers: "))
try:
    if int(x) == int(x[::-1]) :
        print("This number is a Palindrome")
    else: print("This number is not a Palindrome")
except:
    print("Error")        
