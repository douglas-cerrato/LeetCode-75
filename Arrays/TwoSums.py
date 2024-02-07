# TwoSums LeetCode Question
# https://leetcode.com/problems/two-sum/description/

# Task: 
# Given an array of integer nums and an integer target, return indices of the two numbers 
# such that they add up to target.

# Here is an example:
# nums = [2, 7, 11, 15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0,1].

def twoSum(nums, target):
    for index, number in enumerate(nums):
        for index2, number2 in enumerate(nums):
            if((index != index2) and (number+number2 == target)):
               return [index, index2]

def main():

    nums1 = [2,7,11,15]
    target1 = 9
    
    nums2 = [3,2,4]
    target2 = 6

    nums3 = [3,3]
    target3 = 6

    print("Test Case 1: {}".format([0,1] == twoSum(nums1, target1)))
    print("Test Case 2: {}".format([1,2] == twoSum(nums2, target2)))
    print("Test Case 3: {}".format([0,1] == twoSum(nums3, target3)))

main()
