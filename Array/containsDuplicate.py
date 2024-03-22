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


print("Test Case 1: ", containsDuplicate([1,2,3,1])==True)
print("Test Case 2: ", containsDuplicate([1,2,3,4])==False)
print("Test Case 3: ", containsDuplicate([1,1,1,3,3,4,3,2,4,2])==True)
