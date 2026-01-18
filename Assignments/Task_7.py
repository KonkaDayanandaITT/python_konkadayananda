n = int(input("Enter the ordered MxM matrix:"))
matrix = []

for i in range(n):
    row=[]
    for j in range(n):
        row.append(int(input()))
    matrix.append(row)

for i in range(n):
    temp = matrix[i][i]
    matrix[i][i] = matrix[i][n-1-i]
    matrix[i][n-1-i] = temp

for row in matrix:
    print(row)
