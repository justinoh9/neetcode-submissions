class Solution:
    def isPalindrome(self, s: str) -> bool:
        # trying to do it with two pointer
        # most likely use a while loop
        left = 0
        right = len(s)-1
        while left < right:
            while left < right and not ("a" <= s[left] <= "z" or "0" <= s[left] <= "9" or "A" <= s[left] <= "Z"):
                left += 1
            while left < right and not ("a" <= s[right] <= "z" or "0" <= s[right] <= "9" or "A" <= s[right] <= "Z"):
                right -= 1
            if left < right and s[left].lower() != s[right].lower():
                return False
            left, right = left+1, right-1


        return True
