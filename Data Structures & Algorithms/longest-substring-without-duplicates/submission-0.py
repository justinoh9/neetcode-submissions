class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # most likely need to use sliding window
        # need to keep track of longest substring
        # so use a set
        res = 0
        seen = set()
        left = 0 # left pointer
        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            seen.add(s[right])
            res = max(res, right - left + 1)
        return res