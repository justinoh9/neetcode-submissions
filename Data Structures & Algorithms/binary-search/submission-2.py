class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # now i know >:)
        # so the main idea is to use a midpoint
        # we have 2 pointers a left and a right
        left = 0
        right = len(nums)-1
        # and our condition for while loop is when the left pointer is greater than right pointer
        # and our return is the index of the target
        while left <= right:
            # implement midpoint
            mid = (left+right)//2
            # case 1: check if the target is equal to the nums[midpoint]
            if target == nums[mid]:
                return mid
            # case 2: check if the target is fewer than midpoint
            elif target > nums[mid]:
                left = mid+1 # we do + 1 because we have already checked that target != mid
            # case 3: check if the target is greater than midpoint
            elif target < nums[mid]:
                right = mid-1 # same concept as case 2
        # case 4: target not in list
        return -1