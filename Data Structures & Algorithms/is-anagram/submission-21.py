class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        charFreqS = {}
        charFreqT = {}

        n = len(s)
        for i in range(n):
            charFreqS[s[i]] = charFreqS.get(s[i], 0) + 1
            charFreqT[t[i]] = charFreqT.get(t[i], 0) + 1
        
        return charFreqS.items() == charFreqT.items()
