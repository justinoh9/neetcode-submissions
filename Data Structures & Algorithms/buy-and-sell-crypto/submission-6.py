class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # sliding window
        profit = 0
        # want to iterate through whole window to check every value
        # O(n) tc
        left = 0
        n = len(prices)
        for right in range(n):
            profit = max(profit, prices[right] - prices[left])
            if prices[left] > prices[right]:
                left = right
        return profit