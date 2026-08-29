class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # k is the size
        
        stack = []
        
        seen = {}

        res = []

        maxFreq = 0

        for i in range(len(nums)):
            seen[nums[i]] = seen.get(nums[i], 0) + 1
            # key = value, value = freq
        for num, count in seen.items():
            stack.append([count,num])
        stack.sort()

        for k in range(k):
            res.append(stack.pop()[1])
        return res