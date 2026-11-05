class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        '''
        bucket sort alg

        '''
        ans = []
        numFreq = {}

        for i, num in enumerate(nums):
            if num in numFreq:
                numFreq[num] += 1
            else:
                numFreq[num] = 1
        
        buckets = [ [] for _ in range(len(nums) + 1) ] 

        for num, freq in numFreq.items():
            buckets[freq].append(num)

        for i in range(len(buckets) -1, 0, -1):
            for num in buckets[i]:
                ans.append(num)
                if len(ans) == k:
                    return ans
        return ans
