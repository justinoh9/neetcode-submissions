class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # binary search
        # most likely need to implement a two pointer approach
        # use a midpoint
        # (L+R)//2 
        # need to iterate from oen side to other, but not contiguously so use a while loop
        lo = 0
        hi = len(nums) - 1
        while lo <= hi:
            mid = (lo+hi)//2
            # case 1: if target == midpoint
            if target == nums[mid]:
                return mid
            # case 2: if target is lower than midpoint
            elif target < nums[mid]:
                hi = mid - 1
            # case 3: if target is higher than the midpoint
            elif target > nums[mid]:
                lo = mid + 1
            
        return -1
            
