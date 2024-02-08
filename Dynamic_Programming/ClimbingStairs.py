# Climbing Stairs Dynamic Programming
# Problem:
# You are climbing a staircase. It takes n steps to reach the top.
# Each time you either climb 1 or 2 steps. In how many distinct ways can you climb
# to the top?

# Example 1:
# Input: n = 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps

# Example 2:
# Input: n = 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step


def climbStairs(n: int) -> int:
    differentWays = 0
    firstCase = [1 for x in range(n)]
    
    # SUGGESTION: I believe one way we can tackle this idea has something to do with finding 
    # patterns with in our first case list. We know no matter what that every entry will have
    # atleaast one route where we consecutively take 1 step to reach n. So we could find some
    # way where we look for two consecutive ones, and swap them for a 2. However, currently
    # not sure how I am going to do this to find different ways where a list can hold 
    # consecutive 2 steps to reach n

def main():
    print("Test Case 1: {}".format(climbStairs(2)==2))
    print("Test Case 2: {}".format(climbStairs(3)==3))
    print("Test Case 3: {}".format(climbStairs(7)==21))
    print("Test Case 4: {}".format(climbStairs(10)==89))

main()
