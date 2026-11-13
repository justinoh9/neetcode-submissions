class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        stones.sort()

        while len(stones) > 1:
            
            if stones[-1] == stones[-2]:
                stones.pop()
                stones.pop()
            elif stones[-1] > stones[-2]:
                temp = stones[-2]
                del stones[-2]
                stones[-1] = stones[-1] - temp
                stones.sort()
            

        if len(stones) == 1:
            return stones[0]
        
        if len(stones) == 0:
            return 0
        
            