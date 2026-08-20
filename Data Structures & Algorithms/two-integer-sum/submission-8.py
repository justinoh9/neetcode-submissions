class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # iirc, use a dict here where the keys are values, and values are indexes
        seen = {}

        # first populate

        for i in range(len(nums)):
            seen[nums[i]] = i
        
        # now check

        for j in range(len(nums)):
            if (target - nums[j] in seen) and j != seen[target - nums[j]]:
                return [j, seen[target - nums[j]]]
        