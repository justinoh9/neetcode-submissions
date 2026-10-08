class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # probably want a dictionary storing values that we've seen
        # so that we can do math on the numbers that we've seen and return a values
        valInd = {}

        # fill dict
        for i, val in enumerate(nums):
            valInd[val] = i

        # now we can perform math on dict to get missing piece
        for i in range(len(nums)):
            if target-nums[i] in valInd and i != valInd[target - nums[i]]:
                return [i, valInd[target-nums[i]]]
