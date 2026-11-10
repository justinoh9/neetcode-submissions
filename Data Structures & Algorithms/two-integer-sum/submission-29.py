class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #1p

        valInd = {}
        for i, val in enumerate(nums):
            complement = target - val
            if complement in valInd and valInd[complement] != i:
                return [valInd[complement], i]
            valInd[val] = i
        return []