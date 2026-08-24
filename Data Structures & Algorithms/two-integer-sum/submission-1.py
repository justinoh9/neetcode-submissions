class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i in range(len(nums)):
            if nums[i] not in seen:
                seen[nums[i]] = i
            need = target - nums[i]
            if need in seen:
                if seen[need] != i:
                    return [seen[need], i]
        

            


    # return the indices of the values that add up to target
    # use a hash set, or a map or whatever
    # first add all first elements into the map with their indices, then
    # then use math and return indices
            
                
