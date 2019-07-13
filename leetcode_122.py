# 122. Best Time to Buy and Sell Stock II

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        totalProfit = 0
        for index in range(1, len(prices)):
            profit = prices[index] - prices[index - 1]
            if profit > 0:
                totalProfit += profit
        return totalProfit
