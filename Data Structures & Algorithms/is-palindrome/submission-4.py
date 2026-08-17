class Solution:
    def isPalindrome(self, s: str) -> bool:
        # need to sort string first
        clean = ""
        cleanReversed = ""
        for char in s:
            if "a" <= char <= "z" or "0" <= char <= "9":
                # clean.append(char)
                clean = clean + char
                cleanReversed = char + cleanReversed
            if "A" <= char <= "Z":
                clean = clean + char.lower()
                cleanReversed = char.lower() + cleanReversed

        return clean == cleanReversed
            