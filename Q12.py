List = (input("Input number seperate by space: "))
try:
    List = List. split()
    List = [int(num)for num in List]

    print(f"These are sum and average of this list {sum(List)}, {sum(List)/len(list)}")
except:
    print("Error")