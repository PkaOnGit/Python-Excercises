m = int(input("Mathemetics marks = "))
p = int(input("Physics marks = "))
c = int(input("Chemistry marks = "))

if m + p + c >= 200 and m >= 60 and p >= 50 and c >= 40:
                print("Qualified")
elif m + p >= 150 :
    print("Qualified")
else : print("Not Qualified")

