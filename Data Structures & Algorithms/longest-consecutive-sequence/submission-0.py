class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #have a set of seen numbers,
        # have two pointers, one for smaller and one for bigger
        res = 0

        mp = defaultdict(int)
        # for i in nums:
        #     if i not in seen:
        #         seen.append(i)
            
        # for j in range(len(nums)):
            
        #     k = j-1
        #     if k in seen:
        for num in nums:
            if not mp[num]:
                mp[num] = mp[num - 1] + mp[num + 1] + 1
                mp[num - mp[num - 1]] = mp[num]
                mp[num + mp[num + 1]] = mp[num]
                res = max(res, mp[num])
        return res


        