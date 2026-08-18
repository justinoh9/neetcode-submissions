class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # two pointer or sliding window potentially
        # for best profit, should most likely use max function
        # left pointer can be the global min day
        maxProfit = 0
        minIndex = 0
        # want to check every day so can use a for loop
        for currentDay in range(len(prices)):
            # need to keep track of the minimum 
            if prices[minIndex] > prices[currentDay]:
                minIndex = currentDay
            else: # we use an else here because you have to sell the coin on a different day, so mutually exlusive
                maxProfit = max(maxProfit, prices[currentDay] - prices[minIndex]) # using max function to "look" for the best day to sell
        return maxProfit