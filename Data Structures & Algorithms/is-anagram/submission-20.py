class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        charS, charT = {}, {}
        n = len(s)
        for i in range(n):
            charS[s[i]] = charS.get(s[i], 0) + 1
            charT[t[i]] = charT.get(t[i], 0) + 1
        
        return charS.items() == charT.items()