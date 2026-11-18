class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numInd = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in numInd and numInd[complement] != i:
                return [numInd[complement], i]
            numInd[nums[i]] = i
        return []