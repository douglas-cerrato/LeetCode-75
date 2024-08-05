def spiralOrder(matrix: list[list[int]]) -> list[int]:
    return [0,0]


matrix1 = [[1,2,3],[4,5,6],[7,8,9]]
matrix2 = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]

print("Test Case 1: ", spiralOrder(matrix1)==[1,2,3,6,9,8,7,4,5])
print("Test Case 2: ", spiralOrder(matrix2)==[1,2,3,4,8,12,11,10,9,5,6,7])