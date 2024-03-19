def setZeroes(matrix: list[list[int]]) -> None:
    zeroPositionsX = []
    zeroPositionsY = []
    for indexRow, row in enumerate(matrix):
        for indexColumn, column in enumerate(row):
            if(column == 0):
                zeroPositionsX.append(indexRow)
                zeroPositionsY.append(indexColumn)

    # In the leetcode problem, we edit the matrix passed up and 
    # it analyzes the test cases from the matrix edits made. In 
    # my version for testing we make a copy, edit the copy and 
    # return it for comparison
    newMatrix = matrix.copy()      
    
    for indexX, x  in enumerate(newMatrix):
        # Check to see if indexPosition matches with zero position
        # inside of our zeroPositionY list
        for indexY, y in enumerate(x):
            # Iterate through our X positions that have 0, and compare it to 
            # our current index we are looking at X wise. If they match,
            # turn that variable into 0
            for zeroX in zeroPositionsX:
                if zeroX == indexX:
                    newMatrix[indexX][indexY] = 0
            
            # Iterate through our Y positions that have 0, and compare it to 
            # our current index we are looking at Y wise. If they match,
            # turn that variable into 0
            for zeroY in zeroPositionsY:
                if zeroY == indexY:
                    newMatrix[indexX][indexY] = 0

    return newMatrix

# Based on X and Y position, all matching index variables
# will be turned into 0

Case1 = [[1,1,1],[1,0,1],[1,1,1]]
Case2 = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]

print("Test Case 1: ", setZeroes(Case1) == [[1,0,1],[0,0,0],[1,0,1]])
print("Test Case 2: ", setZeroes(Case2) == [[0,0,0,0],[0,4,5,0],[0,3,1,0]])