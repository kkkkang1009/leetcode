# 121. Best Time to Buy and Sell Stock
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        minPrice = float('inf')
        for price in prices:
            minPrice = min(minPrice, price)
            profit = max(profit, price - minPrice)
        return profit