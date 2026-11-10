class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # sliding window
        # O(n) time complexity
        # linearly search through prices arr to find min max

        maxProfit = 0
        left = 0
        n = len(prices)
        for right in range(n):
            maxProfit = max(maxProfit, prices[right] - prices[left])
            if prices[left] > prices[right]:
                left = right
                
        return maxProfit