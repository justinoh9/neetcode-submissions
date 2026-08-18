class Solution:
    def isPalindrome(self, s: str) -> bool:
        # can use .isalnum()

        newString = ""
        newStringReversed = ""
        # def isAlphanumeric(self, char: str) -> str:
        for i in range(len(s)):

            if "a" <= s[i] <= "z" or "0" <= s[i] <= "9":
                newString = newString + s[i]
                newStringReversed = s[i] + newStringReversed
            elif "A" <= s[i] <= "Z":
                newString = newString + s[i].lower()      
                newStringReversed = s[i].lower() + newStringReversed      
            
        return newString == newStringReversed
