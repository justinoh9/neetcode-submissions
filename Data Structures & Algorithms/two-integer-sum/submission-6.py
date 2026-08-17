class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # know that we need to use dict
        # key can be the value of the index
        # value can be index 
        # need to do a first pass to populate the seen dictionary
        seen = {}
        for i in range(len(nums)):
            seen[nums[i]] = i
        # now we need to find the matching index pair for the target
        # know that target = nums[i] + nums[j] and i != j
        for j in range(len(nums)):
            # know that we can rearrange nums[i] = target - nums[j]
            if target - nums[j] in seen and j != seen[target-nums[j]]:
                return [j, seen[target-nums[j]]]