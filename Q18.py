try:
    x = list(input("Enter number seperate each number with space: " ).split( ))

    for i in x:
        if not type(int(i)) is int:
            raise TypeError
            

    print(f"smallest number {min(x)} and biggest number {max(x)}")

except:
    print("Error")