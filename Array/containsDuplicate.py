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
                #print(f"indexX is < len(nums), our variable we are looking at is {x} > {nums[indexX+1]}")
                for y in range(0, indexX+1):
                    print(f"\nList before the swap {nums}")
                    #print(f"range from the back to the front is {(indexX+1) - y}")
                    #print(f"The variable we are currently looking at before swap is {nums[(indexX) - y]}")
                    tempVar = nums[(indexX+1) - y]
                    nums[(indexX+1) - y] = nums[(indexX) - y]
                    nums[(indexX) - y] = tempVar
                    print(f"\nList is {nums}")
                    print("\n\nBefore the if to see if there is a match\n---------------------------------")

                    print(f"\nindexX - y is {indexX - y} or tempVar {tempVar} > {nums[(indexX - 1) - y]} nums[(indexX - 1) - y]")
                    if((indexX - y) == 0 or (tempVar > nums[(indexX-1) - y])):
                        if(tempVar == nums[(indexX-1)]):
                            print("tempVar: {} nums[(indexX-1)]: {}".format(tempVar, nums[(indexX-1)]))
                            print("List after finding a duplicate: ", nums)
                            return True
                        break

    print("List after being sorted: ", nums)
    return False

print("Test Case 1: ", containsDuplicate([1,2,3,1])==True)
print("Test Case 2: ", containsDuplicate([1,2,3,4])==False)
print("Test Case 3: ", containsDuplicate([1,1,1,3,3,4,3,2,4,2])==True)
print("Test Case 4: ", containsDuplicate([1,5,-2,-4,0])==False)
