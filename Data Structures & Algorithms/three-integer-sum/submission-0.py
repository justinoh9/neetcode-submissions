class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()

        for x in range(len(nums)):
            seen = set()

            for y in range(x + 1, len(nums)):
                z = -nums[x] - nums[y]

                if z in seen:
                    triplet = tuple(sorted([nums[x], nums[y], z]))
                    res.add(triplet)

                seen.add(nums[y])

        return [list(triplet) for triplet in res]