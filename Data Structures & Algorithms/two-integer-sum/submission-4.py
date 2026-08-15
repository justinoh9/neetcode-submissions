class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        
        for i in range(len(nums)):
            seen[nums[i]] = i
        for j in range(len(seen)):
            if target - nums[j] in seen and j != seen[target - nums[j]]:
                return [j, seen[target - nums[j]] ]
        

