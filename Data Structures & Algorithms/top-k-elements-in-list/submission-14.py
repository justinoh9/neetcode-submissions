class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # want to return the msot frequent number
        # frequency is dict and list
        
        numFreq = {}

        # sort the numbers into the dict with the freq being a list

        # 1

        for i, num in enumerate(nums):
            numFreq[num] = numFreq.get(num, 0) + 1

        # now create the bucket lists

        buckets = [ [] for _ in range(len(nums) + 1) ] 
        
        for num, freq in numFreq.items():
            buckets[freq].append(num)

        res = []

        # iterate through buckets from highest to lowest freq

        for bucket in range(len(buckets) - 1, 0, -1):
            for num in buckets[bucket]:
                res.append(num)
                if len(res) == k:
                    return res
        return res