class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # global min
        lowestDay = 0
        # best profit
        bestProfit = 0
        # want to iterate over list to check every day
        for potentialSellDay in range(len(prices)):
            if prices[lowestDay] > prices[potentialSellDay]:
                lowestDay = potentialSellDay
            else: # want mutual exclusive b/c can only buy sell on one day
                bestProfit = max(bestProfit, prices[potentialSellDay] - prices[lowestDay])
        return bestProfit