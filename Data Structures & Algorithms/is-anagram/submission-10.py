class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #use a dict
        sDict = {}
        tDict = {}
        # need to compare frequency of characters in each string
        # fill each dict
        # key = char
        # value = count
        # edge case if they aren't same length
        if len(s) != len(t):
            return False
        
        for i in range(len(s)):
            sDict[s[i]] = sDict.get(s[i], 0) + 1 # remember, it isn't items, because items() returns the items. its actually get to access
            tDict[t[i]] = tDict.get(t[i], 0) + 1
        
        return sDict.items() == tDict.items()