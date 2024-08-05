def spiralOrder(matrix: list[list[int]]) -> list[int]:
    # Point of Function is to spiral through a matrix,
    # and return the value in each index in a ordered list 
    
    # If we were to view the matrix in a way where each value
    # is the index inside the matrix, it would like something 
    # like this:
    
    # 00  01  02                00  01  02  03
    # 10  11  12       or       10  11  12  13   
    # 20  21  22                20  21  22  23
    #                           30  31  32  33

    # Therefore, we can use this understanding to figure out how
    # we would go about navigating this matrix. This will help us
    # in terms of spiraling it. 

    # To iterate through the matrix by a direction. Here is how 
    # we would do it.

    # Assuming we view each index in this matrix as a (x,y) coordinate

    # Right: y + 1
    # Down: x + 1
    # Left: y - 1
    # Up: x - 1

    # This would mean we would have to add one position unit to either x or y
    # to view the current value at that coordinate. So now just need to figure out
    # how to spiral through the matrix (with hopes of doing with the fastest time
    # complexity)

    for index, value in enumerate(matrix):
        print(f"Index: {index} Value {value}")

    return [0,0]


matrix1 = [[1,2,3],[4,5,6],[7,8,9]]
matrix2 = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]

print("Test Case 1: ", spiralOrder(matrix1)==[1,2,3,6,9,8,7,4,5])
print("Test Case 2: ", spiralOrder(matrix2)==[1,2,3,4,8,12,11,10,9,5,6,7])