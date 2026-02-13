def swap_diagonals(matrix):
    size = len(matrix)
    for i in range(size):
        temp = matrix[i][i]
        matrix[i][i] = matrix[i][size - 1 - i]
        matrix[i][size - 1 - i] = temp

    return matrix


size = int(input("Enter the ordered MxM matrix:"))
matrix = []

for row_index in range(size):
    row = []
    for column_index in range(size):
        row.append(int(input()))
    matrix.append(row)

result = swap_diagonals(matrix)

for row in result:
    print(row)
