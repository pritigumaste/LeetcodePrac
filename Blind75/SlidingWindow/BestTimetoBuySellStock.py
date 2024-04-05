#kadane's algo

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #one pass approach
        maxProfit =0
        minPrice = float('inf')
       
        for i in range(len(prices)):
            if prices[i] < minPrice:
                minPrice = prices[i]
            elif prices[i] - minPrice > maxProfit:
                maxProfit = prices[i] - minPrice
        return maxProfit
