class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # first we need to catagorize numbers by freq

        numFreq = {}
        for i in range(len(nums)):
            numFreq[nums[i]] = numFreq.get(nums[i], 0) + 1

        # next, create buckets to sort the frequencies

        buckets = [ [] for i in range(len(nums) + 1) ]

        # then, sort the numbers by their frequencies into the buckets

        for num, freq in numFreq.items():
            buckets[freq].append(num)
        
        # finally, return the highets freq num k times

        res = []
        
        for i in range(len(buckets) - 1, 0, -1):

            for num in buckets[i]:

                res.append(num)
                if len(res) == k:
                    return res
        return res
