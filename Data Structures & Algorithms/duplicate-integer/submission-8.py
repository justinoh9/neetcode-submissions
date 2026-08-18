class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # i remember that this one uses a set 
        seen = set()
        for i in range(len(nums)):
            if nums[i] not in seen:
                seen.add(nums[i])
            else:
                return True
        return False