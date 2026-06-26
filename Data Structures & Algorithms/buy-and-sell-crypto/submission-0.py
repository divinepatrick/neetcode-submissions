class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        lowest_price = prices[0]

        for i in range(len(prices)):
            lowest_price = min(prices[i], lowest_price)
            profit = prices[i] - lowest_price
            max_profit = max(max_profit, profit)
        return max_profit