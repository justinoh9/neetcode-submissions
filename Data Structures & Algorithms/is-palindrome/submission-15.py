class Solution:
    def isPalindrome(self, s: str) -> bool:
        lo = 0
        hi = len(s) - 1

        while lo < hi:

            # Skip non-alphanumeric characters from left
            while lo < hi and not s[lo].isalnum():
                lo += 1

            # Skip non-alphanumeric characters from right
            while lo < hi and not s[hi].isalnum():
                hi -= 1

            # Compare characters (case insensitive)
            if s[lo].lower() == s[hi].lower():
                lo += 1
                hi -= 1
            else:
                return False

        return True