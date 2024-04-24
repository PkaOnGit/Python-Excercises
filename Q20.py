try:
    print("This version can only sum matrix with the same size\ninsert info of matrix 1")
    Column1 = int(input("Insert column : "))
    Row1 = int(input("Insert row: "))

    print("insert info of matrix 2")
    Column2 = int(input("Insert column : "))
    Row2 = int(input("Insert row: "))

    if Column1 != Column2 and Row1 != Row2:
        exit()
    

    if not type(Row1 and Row2 and Column1 and Column2) is int :
        raise TypeError("Error")
    
    matrix1 = []

    for row in range(0,Row1):
        row = []
        a = None
        for column in range(0,Column1):
            a = int(input("Number in the matrix 1: "))
            row.append(a)
        matrix1.append(row)

    matrix2 = []

    for row in range(0,Row2):
        row = []
        for column in range(0,Column2):
            b = int(input("Number in the matrix 2:"))
            row.append(b)
        matrix2.append(row)

    if not type(a and b) is int :
        raise TypeError("Error")

    result = [[matrix1[row][column] + matrix2[row][column]  
            for column in range(len(matrix1[0]))] 
            for row in range(len(matrix2))]

    for r in result:
        print(r)
except:
    print("error")