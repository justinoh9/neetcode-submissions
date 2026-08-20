class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # if our goal is to find the index value that is equal to target
        # need binary search if logn time
        # midpoint
        # two pointer approach

        lo = 0
        hi = len(nums) - 1
        while lo <= hi:
            mid = (lo+hi)//2
            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                lo = mid+1
            elif target < nums[mid]:
                hi = mid-1
        return -1