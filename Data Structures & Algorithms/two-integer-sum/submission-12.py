class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        store = {}

        for i in range(len(nums)):
            store[nums[i]] = i

        for j in range(len(nums)):
            if target - nums[j] in store and j != store[target - nums[j]]:
                return [j, store[target - nums[j]]]
        return []