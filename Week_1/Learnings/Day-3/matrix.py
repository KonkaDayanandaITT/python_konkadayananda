#Matrix : a matrix is a list of lists
import numpy as np

matrix = [
    [1,2,3],
    [3,4,5]
]

print(matrix[0][0])
print(matrix)

for i in matrix:
    for j in i:
        print(j,end=" ")
    print()

mat = np.array([
    [1,2,3],
    [4,5,6]
])
print(mat.shape)
