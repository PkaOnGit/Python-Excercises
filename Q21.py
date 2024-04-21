print("insert info of matrix 1")
Column1 = int(input("Insert column : "))
Row1 = int(input("Insert row: "))


print("insert info of matrix 2")
Column2 = int(input("Insert column : "))
Row2 = int(input("Insert row: "))

if Column1 != Row2:
    print("Error.")
    exit()

matrix1 = []

for Row in range(0,Row1):
    row = []
    for Column in range(0,Column1):
        a = int(input("Number in the matrix 1: "))
        row.append(a)
    matrix1.append(row)

matrix2 = []

for Row in range(0,Row2):
    row = []
    for Column in range(0,Column2):
        a = int(input("Number in the matrix 2:"))
        row.append(a)
    matrix2.append(row)

 
result = [[0] * Column2 for _ in range(Row1)]

for Row in range(Row1):
    for Column in range(Column2):
        for x in range(Column1):
            result[Row][Column] += matrix1[Row][x] * matrix2[x][Column]
print("Result")
print(result)
