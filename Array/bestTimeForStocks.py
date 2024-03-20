def maxProfit(prices: list[int]) -> int:
    highestPrice = 0
    for indexX, x in enumerate(prices):
        for y in range(indexX+1, len(prices)):

            if (x < prices[y]):
                tempPrice = prices[y] - x
                if(tempPrice > highestPrice): 
                    highestPrice = tempPrice
    
    return highestPrice

print("Test Case 1", maxProfit([7,1,5,3,6,4]) == 5)
print("Test Case 2", maxProfit([7,6,4,3,1]) == 0)