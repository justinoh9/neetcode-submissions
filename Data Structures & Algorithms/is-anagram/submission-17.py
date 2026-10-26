class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # sort arr return
        # use dict count char freq
        charFreqS = {}
        charFreqT = {}
        if len(s) != len(t):
            return False
        
        for i in range(len(s)):
            charFreqS[s[i]] = charFreqS.get(s[i], 0) + 1
            charFreqT[t[i]] = charFreqT.get(t[i], 0) + 1
        
        return charFreqS == charFreqT