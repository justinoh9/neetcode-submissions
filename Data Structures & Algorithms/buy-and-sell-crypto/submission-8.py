class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        left = 0
        n = len(prices)
        for right in range(n):
            profit = max(profit, prices[right] - prices[left])
            if prices[left] > prices[right]:
                left = right


        return profit
