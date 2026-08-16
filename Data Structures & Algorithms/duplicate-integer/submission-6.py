class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        appears = set() # using a set because it measures frequency at constant time
        # need to figure out what is in list, while checking what has already been seen
        for i in range(len(nums)):
            #check if has been seen yet
            if nums[i] not in appears:
                appears.add(nums[i])
            else:
                return True
        return False