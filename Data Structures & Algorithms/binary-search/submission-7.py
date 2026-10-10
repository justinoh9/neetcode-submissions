class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # given list of numbers sorted in ascending ordewr
        # implement binary search
        # similar to a two pointer approach, two bounds
        lo = 0
        hi = len(nums) - 1 

        while lo <= hi:
            mid = ((lo + hi) // 2) 
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                lo = mid + 1
            else:
                hi = mid - 1
        
        
        return -1