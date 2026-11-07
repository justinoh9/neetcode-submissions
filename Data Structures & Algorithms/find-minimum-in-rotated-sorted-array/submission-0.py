class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        while nums[left] > nums[right] and left < right:
            mid = (left + right) // 2

            if nums[mid] > nums[left]:
                left = mid
            elif nums[mid] < nums[right]:
                right = mid
            else:
                left += 1
                right -= 1

        return min(nums[left], nums[right])