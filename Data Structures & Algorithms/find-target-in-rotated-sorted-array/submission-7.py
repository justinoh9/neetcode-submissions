class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        def binSearch(l,r):
            while l <= r:
                m = (l + r) // 2
                if target == nums[m]:
                    return m
                elif target > nums[m]:
                    l = m + 1
                else:
                    r = m - 1
            return -1
        def findRotation(l, r):
            while l < r:
                m = l + (r - l) // 2

                if nums[m] > nums[r]:
                    l = m + 1
                else:
                    r = m

            return l
        left = 0
        right = len(nums) - 1

        rotationIndex = findRotation(left, right)

        if rotationIndex == 0:
            return binSearch(left, right)
        elif target >= nums[0]:
            return binSearch(left, rotationIndex - 1)
        else:
            return binSearch(rotationIndex, right)