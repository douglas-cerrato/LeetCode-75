def containsDuplicate(nums: list[int]) -> bool:
        for indexX, x in enumerate(nums):
            newNums = nums[indexX+1:]
            print(f"newNums is {newNums}")
            if(x in newNums):
                return True
        
        return False


print("Test Case 1: ", containsDuplicate([1,2,3,1])==True)
print("Test Case 2: ", containsDuplicate([1,2,3,4])==False)
print("Test Case 3: ", containsDuplicate([1,1,1,3,3,4,3,2,4,2])==True)
