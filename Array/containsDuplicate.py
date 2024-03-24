def containsDuplicate(nums: list[int]) -> bool:
    for indexX, x in enumerate(nums):
        if indexX < len(nums) - 1:
            # Declaring index of the Value ahead of X, which we
            # use to compare to see if we need to sort the number
            # into the correct position
            frontOfX = indexX+1
            if x < nums[frontOfX]:
                continue
            else:
                # Creating a list from 0 to the variable infront of X
                for y in range(0, frontOfX):

                    # Declaring inverse index so we compare values from the 
                    # end of the list and work our way to the front
                    inverseOfFOX = frontOfX - y # inverseOfFrontOFX
                    inverseOfXI = indexX - y #inverseOfXIndex

                    # Swapping the number at the end of the list 
                    # with the variable before it
                    print(f"Nums is {nums}")
                    print(f"\n\nInverse of Front of X Index: {inverseOfFOX} Value: {nums[inverseOfFOX]}")
                    print(f"Inverse of X Index: {inverseOfXI} Value: {nums[inverseOfXI]}\n\n")
                    tempVar = nums[inverseOfFOX]
                    nums[inverseOfFOX] = nums[inverseOfXI]
                    nums[inverseOfXI] = tempVar

                    print(f"\n\n\n FOR TESTING: tempVar AFTER THE ABOVE SWAP ^^^^ IS: {tempVar}\n\n\n")

                    print(f"After the swap the list is {nums}")

                    # If we moved this number to the first position in the list
                    if(inverseOfXI == 0):
                        break
                    
                    inverseOfBOX = (indexX-1) - y #inverseOfBackOfXI
                    print(f"tempVar after the swap is {tempVar} and valueBeforeX is {nums[inverseOfBOX]}")

                    if((indexX - y) == 0 or (tempVar > nums[(indexX-1) - y])):
                        if(tempVar == nums[(indexX-1)]):
                            return True
                        break

    print("List after being sorted: ", nums)
    return False

print("Test Case 1: ", containsDuplicate([1,2,3,1])==True)
print("Test Case 2: ", containsDuplicate([1,2,3,4])==False)
print("Test Case 3: ", containsDuplicate([1,1,1,3,3,4,3,2,4,2])==True)
print("Test Case 4: ", containsDuplicate([1,5,-2,-4,0])==False)
