class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # i nkow i have to use a dict
        # need to return indices
        # make the key the value
        # make value the index
        # first fill dict with values in list
        # we make the key the value because index cannot repeat
        seen = {}
        for index in range(len(nums)):
            seen[nums[index]] = index
        
        # now we do a second pass to check if int in list completes to target
        for i in range(len(nums)):
            # need to find index
            if target - nums[i] in seen and i != seen[target-nums[i]]:
                return [i, seen[target-nums[i]]]
                