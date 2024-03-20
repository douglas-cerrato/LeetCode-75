def maxProfit(prices: list[int]) -> int:
    highestPrice = 0
    lowCount = None
    for indexX, x in enumerate(prices):
        
        if(lowCount == None):
            lowCount = indexX
            continue

        if(lowCount != indexX):
            if(x < prices[lowCount]):
                lowCount = indexX

        if((x - prices[lowCount]) > highestPrice):
            highestPrice =  x - prices[lowCount]
    
    return highestPrice

print("Test Case 1: ", maxProfit([7,1,5,3,6,4]) == 5)
print("Test Case 2: ", maxProfit([7,6,4,3,1]) == 0)