def containsDuplicate(nums: list[int]) -> bool:
    for indexX, x in enumerate(nums):
        if indexX < len(nums) - 1:
            if x < nums[indexX+1]:
                continue
            else:
                # Iterate and compare / swap until the number ahead is bigger and
                # the number behind is smaller. If the number behind is ever equal
                # to the number we are passing down, then return True, else when full
                # list is sorted, return False
                
                # Here we use y in a for loop from the beginning of the list to position x
                # with the intention of iterating backwards through the list starting at indexX + 1
                # We are iterating backwards so we can get the smaller number in the comparison,
                # and move it backwards until it is in the correct position it needs to be in 
                print(f"The variable that started this chain is X: {x}")
                for y in range(0, indexX+1):
                    print(f"Before the swap is the variable we are at is {nums[indexX - y]} and the variable ahead that is smaller is {nums[(indexX+1) - y]}")
                    print(f"Before the swap the list is {nums}")
                    tempVar = nums[(indexX+1) - y]
                    nums[(indexX+1) - y] = nums[(indexX) - y]
                    nums[(indexX) - y] = tempVar

                    print(f"After the swap the list is {nums}")
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
