class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # need to find length of longest substring w/out dup
        # returning an int, so
        res = 0
        # must be contiguous, leads me to use a sliding window
        l = 0
        # without duplicate concept can be tackled with a set
        seen = set()
        # iterate over string using two pointer
        for r in range(len(s)):
            while s[r] in seen:
                #remove left pointer if in seen
                seen.remove(s[l])
                l += 1
            # add right pointer to seen
            seen.add(s[r])
            res = max(res, r - l + 1)
        return res

