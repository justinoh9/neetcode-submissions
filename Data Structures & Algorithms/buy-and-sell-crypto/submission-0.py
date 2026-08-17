class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # aiming to maximize profit.
        '''
        l, h
        10, 10 
        1, 1 if h-l >= prev h-l
        1, 5 if high < prices[r] 
        1, 6 
        1, 7
        1, 7 if 
        
        10  10,10
        2   2,2
        5   2,5
        6   2,6
        1   2,6
        7   1,7
        
        '''

        # res = 0
        # low = 0
        # l = 0
        # for r in range(len(prices)):
        #     # best profit 
        #     if prices[r]-prices[l] >= res:
        #         low = prices[l]
        #         res = prices[r] - low
        #     #lowest
        #     while low >= prices[l]:
        #         low = prices[l]
        #         l += 1
        # return res


        res = 0
        l = 0

        for r in range(len(prices)):

            if prices[r] < prices[l]:
                l = r

            else:
                res = max(res, prices[r] - prices[l])

        return res
