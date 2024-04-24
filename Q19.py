x = list(input("enter number here seperate with space: ").split( ))

even = 0 
odd = 0
try:

    for j in x:
        if not type(int(j)) is int:
            raise TypeError("Error")

    for i in range(0,len(x)):
        if i % 2 == 0:
            even += 1
        else: 
            odd += 1

    print(f"these are number of even and odd number {even},{odd}")

except:
    print("Error")
