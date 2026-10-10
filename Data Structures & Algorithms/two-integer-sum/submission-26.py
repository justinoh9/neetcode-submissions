class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        valInd = {}
        # fill dict with values as index, and index as value

        for i, val in enumerate(nums):
            valInd[val] = i

        # now we need to perform math on each index of the list to find a compatible value that equals target

        for i in range(len(nums)):
            if target - nums[i] in valInd and valInd[target-nums[i]] != i:
                return [i, valInd[target-nums[i]]]
        return []