class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        '''
        first need to use dict to find num freq
        bucket sort for frequent elements
        reverse iterate buckets k times for ans arr
        '''
        #1 
        numFreq = {}
        for num in nums:
            numFreq[num] = numFreq.get(num, 0) + 1

        #2 
        buckets = [ [] for _ in range(len(nums) + 1)] # +1 b/c zero indexed

        # fill buckets
        for num, freq in numFreq.items():
            buckets[freq].append(num)
        
        #3 reverse iterate buckets

        ans = []

        for i in range(len(buckets) - 1, 0, -1):
            for val in buckets[i]:
                ans.append(val)
                if len(ans) == k:
                    return ans
        return ans