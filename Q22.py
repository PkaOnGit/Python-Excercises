x = list(input("enter number here seperate with space: ").split( ))
try:

    Evenlist = []

    for even in x:
        if int(even) % 2 == 0:
            Evenlist.append(str(even))


    Evenlist  = [ int(i) for i in Evenlist ]
    sumeven = sum(Evenlist)

#for i in x:
#    if int(i) % 2 == 0:
#        sumeven += int(i)
#    else: sumeven += 0
    
    print(f"This is sum of even number {sumeven}")

except:
    print("Error")