class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # given s string of uppercase letters
        # given k changes, create the longest string with single character
        # return length of that longest string

        # we want the frequency of each character first
        # do a first pass for each letter
        count = {}
        l = 0
        res = 0
        for r in range(len(s)):
            
            count[s[r]] = count.get(s[r], 0) + 1

            while (r - l + 1) - max(count.values()) > k:
                count[s[l]] = count.get(s[l], 0) - 1
                l += 1

            res = max(res, r - l + 1)

        return res        