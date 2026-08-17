class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # need to return the indices of a list where the values add to the target
        # can use a dictionary
        # key = value 
        # value = index
        seen = {}
        
        #iterate over the list
        for i in range(len(nums)):
            # do a first pass to populate seen
            seen[nums[i]] = i
        
        for j in range(len(nums)):
            if target - nums[j] in seen and j != seen[target - nums[j]]:
                return [j, seen[target - nums[j]] ]