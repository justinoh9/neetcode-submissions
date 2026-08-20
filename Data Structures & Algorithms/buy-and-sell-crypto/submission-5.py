class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # know that we need global min
        # know that we need best profit
        bestProfit = 0
        lo = 0

        for hi in range(len(prices)):
            if prices[lo] > prices[hi]:
                lo = hi
            else:
                bestProfit = max(bestProfit, prices[hi] - prices[lo])
        return bestProfit