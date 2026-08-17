class Solution:
    def isPalindrome(self, s: str) -> bool:
        # first, clean the word
        cleanString = ""
        cleanStringReversed = ""
        for char in s:
            if 'a' <= char <= 'z' or '0' <= char <= '9':
                cleanString = cleanString + char
                cleanStringReversed = char + cleanStringReversed
            elif 'A' <= char <= 'Z':
                cleanString = cleanString + char.lower()
                cleanStringReversed = char.lower() + cleanStringReversed
        
       
        return cleanString == cleanStringReversed