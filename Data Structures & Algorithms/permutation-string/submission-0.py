class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # just need to check if the characters of s1 are in a contiguous string in s2
        
        # probably use a sliding window approach

        

        s1chars = {}
        for c in s1:
            s1chars[c] = s1chars.get(c, 0) + 1

        for i in range(len(s2)):
            if (i + len(s1)) > len(s2):
                return False
            s2chars = {}
            for j in range(len(s1)):
                s2chars[s2[i+j]] = s2chars.get(s2[i+j], 0) + 1
            if s1chars == s2chars:
                return True


        return False