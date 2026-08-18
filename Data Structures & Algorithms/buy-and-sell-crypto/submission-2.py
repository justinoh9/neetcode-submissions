class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # want to keep track of 
        # global min
        # best profit

        lo = 0
        res = 0

        for hi in range(len(prices)):
            #see if global min
            if prices[hi] < prices[lo]:
                lo = hi
            
            # now that i have global min
            # i can try working on best profit
            # its an else lmao what
            else:
                res = max(res, prices[hi] - prices[lo])
        return res  