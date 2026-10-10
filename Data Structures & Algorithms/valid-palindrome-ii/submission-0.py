class Solution:
    def validPalindrome(self, s: str) -> bool:
        if s == s[::-1]:
            return True
        lo = 0
        hi = len(s) - 1
        while lo <= hi:
            templo = s[:lo] + s[lo + 1:]
            if templo == templo[::-1]:
                return True
            temphi = s[:hi] + s[hi + 1:]
            if temphi == temphi[::-1]:
                return True
            lo += 1
            hi -= 1
        return False
