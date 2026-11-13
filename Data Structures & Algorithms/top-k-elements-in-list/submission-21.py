class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # bucket sort

        numFreq = {}
        for num in nums:
            numFreq[num] = numFreq.get(num, 0) + 1

        buckets = [ [] for _ in range(len(nums) + 1) ]

        for num, freq in numFreq.items():
            buckets[freq].append(num)
        
        res = []

        for i in range(len(buckets) - 1, -1, -1):
            for num in buckets[i]:
                res.append(num)
                if len(res) == k:
                    return res
        return res