class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # one pass solution
        valInd = {}
        for i, val in enumerate(nums):
            complement = target - val
            if complement in valInd and valInd[complement] != i:
                return [valInd[complement], i]
            valInd[val] = i
        return []