print("insert info of matrix 1")
Column1 = int(input("Insert column : "))
Row1 = int(input("Insert row: "))

matrix1 = []

for row in range(0,Row1):
    row = []
    a = None
    for column in range(0,Column1):
        a = int(input("Number in the matrix 1: "))
        row.append(a)
    matrix1.append(row)

print("insert info of matrix 2")
Column2 = int(input("Insert column : "))
Row2 = int(input("Insert row: "))


matrix2 = []

for row in range(0,Row2):
    row = []
    for column in range(0,Column2):
        a = int(input("Number in the matrix 2:"))
        row.append(a)
    matrix2.append(row)

result = [[matrix1[row][column] + matrix2[row][column]  
        for column in range(len(matrix1[0]))] 
        for row in range(len(matrix2))]

for r in result:
    print(r)