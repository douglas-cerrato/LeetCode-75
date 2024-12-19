def spiralOrder(matrix: list[list[int]]) -> list[int]:
    if not matrix or not matrix[0]:
        return []  # Handle edge cases where the matrix is empty

    # Initialize boundaries
    top, bottom = 0, len(matrix) - 1
    left, right = 0, len(matrix[0]) - 1
    returnList = []

    # Traverse the matrix while there are elements within the boundaries
    while top <= bottom and left <= right:
        # Traverse from left to right across the top row
        for x in range(left, right + 1):
            returnList.append(matrix[top][x])
        top += 1

        # Traverse from top to bottom down the right column
        for y in range(top, bottom + 1):
            returnList.append(matrix[y][right])
        right -= 1

        # Traverse from right to left across the bottom row (if not already traversed)
        if top <= bottom:
            for x in range(right, left - 1, -1):
                returnList.append(matrix[bottom][x])
            bottom -= 1

        # Traverse from bottom to top up the left column (if not already traversed)
        if left <= right:
            for y in range(bottom, top - 1, -1):
                returnList.append(matrix[y][left])
            left += 1
  
    return returnList


matrix1 = [[1,2,3],[4,5,6],[7,8,9]]
matrix2 = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]

print("Test Case 1: ", spiralOrder(matrix1)==[1,2,3,6,9,8,7,4,5])
print("Test Case 2: ", spiralOrder(matrix2)==[1,2,3,4,8,12,11,10,9,5,6,7])