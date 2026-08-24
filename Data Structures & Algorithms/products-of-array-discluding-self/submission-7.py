class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # res = []
        # for i in nums:
        #     val = 1
        #     for j in nums:
        #         if val == 1 and j == 0:
        #             val = 0
        #         # elif val == 0:
        #         #     val = j
        #         elif j != i:
        #             val *= j
            
        #     res.append(val)
        # return res
        """
        res = []
        for i in range(len(nums)):
            val = 1
            for j in range(len(nums)):
                if j != i: 
                    val *= nums[j]
            res.append(val)
        return res
        """

        res = [1] * (len(nums))

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(len(nums) -1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res
