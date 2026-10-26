class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ans = []
        # iterate through array and count frequencies of each unique number
        valFreq = {}
        for i, val in enumerate(nums):
            valFreq[val] = valFreq.get(val, 0) + 1

        # create buckets to sort most freq to least freq

        buckets = [ [] for _ in range(len(nums) + 1)]

        for val, freq in valFreq.items():
            buckets[freq].append(val)
        
        # iterate through buckets backwards
        for i in range(len(buckets) - 1, 0, -1):
            # iterate through each bucket, and append to ans until k is reached
            for element in buckets[i]:
                ans.append(element)
                if len(ans) == k:
                    return ans
        return ans