class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letterCountS = {}
        letterCountT = {}
        if range(len(s)) != range(len(t)):
            return False
        
        for i in range(len(s)):
            letterCountS[s[i]] = letterCountS.get(s[i], 0) + 1
        for j in range(len(t)): 
            letterCountT[t[j]] = letterCountT.get(t[j], 0) + 1
        if letterCountS == letterCountT:
            return True
        return False

            