class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)-1
        while l <= r:
            if nums[(l+r)//2] == target:
                return (l+r)//2
            elif nums[(l+r)//2] < target:
                l = ((l+r)//2) + 1 
            else:
                r = ((l+r)//2) - 1

        return -1