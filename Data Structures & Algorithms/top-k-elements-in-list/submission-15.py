class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # idea is that we need to return the k most freq elements
        # so we need the number, and we need frequency

        numFreq = {}

        # fill the dict

        for i in range(len(nums)):
            numFreq[nums[i]] = numFreq.get(nums[i], 0) + 1
        
        # now that we havea dict with nums and freq, we need to create buckets to sort by freq

        bucket = [ [] for _ in range(len(nums) + 1) ] 

        # now fill the buckets by freq

        for num, freq in numFreq.items():
            
            bucket[freq].append(num)

        # now we gotta iterate from high to low freq and parse out the numbers by most freq k times

        res = []


        for i in range(len(bucket) - 1, 0, -1):
            for num in bucket[i]:
                res.append(num)
                if len(res) == k:
                    return res
        return res