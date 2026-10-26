class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        valInd = {}
        for i, val in enumerate(nums):
            valInd[val] = i
        for i in range(len(nums)):
            complimentVal = target - nums[i]

            if complimentVal in valInd and valInd[complimentVal] != i:
                return [i, valInd[complimentVal]]