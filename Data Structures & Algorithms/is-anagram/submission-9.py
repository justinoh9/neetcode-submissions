class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # alright this time, no cheese
        # need to return a bool

        # checking if the frequency of characters are equal in each string

        # i believe i can use the char as a key, and value is freq
        # so use dict
        dictS = {}
        dictT = {}

        if len(s) != len(t):
            return False
        for i in range(len(s)):
            dictS[s[i]] = dictS.get(s[i], 0) + 1
            dictT[t[i]] = dictT.get(t[i], 0) + 1
        
        return dictS == dictT