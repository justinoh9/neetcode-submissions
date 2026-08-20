class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # use a dict, where key = char, and value = frequency

        dictS = {}
        dictT = {}

        # fill both dict up
        for i in range(len(s)):
            dictS[s[i]] = dictS.get(s[i], 0) + 1
            
        for j in range(len(t)):
            dictT[t[j]] = dictT.get(t[j], 0) + 1
            
        return dictS == dictT