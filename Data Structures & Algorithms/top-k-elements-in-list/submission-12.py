class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        res = []
        valFreq = {}

        for i in range(len(nums)):
             
            valFreq[nums[i]] = valFreq.get(nums[i], 0) + 1
             
        # now that we have val : freq, we need to put the freq in buckets

        buckets = []

        for i in range(len(nums)+1):
            buckets.append([])
        
        for val, freq in valFreq.items():
            buckets[freq].append(val)
        counter = 0
        for i in range(len(buckets) - 1, 0, -1):
            for val in buckets[i]:
                res.append(val)
                counter += 1
                if counter == k:
                    return res
        
        return res