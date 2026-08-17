class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # definitely using a set here
        # iterate over a list
        # return a bool
        seen = set()
        for i in range(len(nums)):
            if nums[i] not in seen:
                seen.add(nums[i])
            else:
                return True
        return False