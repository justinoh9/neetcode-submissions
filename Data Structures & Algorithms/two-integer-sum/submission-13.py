class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i in range(len(nums)):

            seen[nums[i]] = i
        
        for i in range(len(nums)):

            if target - nums[i] in seen and i != seen[target - nums[i]]:
                return [i, seen[target - nums[i]]]
        return []