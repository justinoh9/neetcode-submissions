class Solution:
    def isPalindrome(self, s: str) -> bool:
        # if "a" <= s[i] <= "z" or "0" <= s[i] <= "9":
        # elif "A" <= s[i] <= "Z":

        # two pointer approach
        rightIndex = len(s) - 1
        leftIndex = 0
        while leftIndex < rightIndex:
            while leftIndex < rightIndex and not ("a" <= s[leftIndex] <= "z" or "0" <= s[leftIndex] <= "9" or "A" <= s[leftIndex] <= "Z"):
                leftIndex += 1
            while leftIndex < rightIndex and not ("a" <= s[rightIndex] <= "z" or "0" <= s[rightIndex] <= "9" or "A" <= s[rightIndex] <= "Z"):
                rightIndex -= 1

            if s[leftIndex].lower() == s[rightIndex].lower():    
                leftIndex += 1
                rightIndex -= 1
            else:
                return False
        return True