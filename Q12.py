List = (input("Input number seperate by space: "))

List = List. split()
List = [int(num)for num in List]

Sum= sum(List)
Ave=  sum(List) / len(List)

print(f"These are sum and average of this list {Sum}, {Ave}")