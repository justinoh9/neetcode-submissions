class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # need to iterate through both words at same time

        w = 0
        res = ''
        while w < len(word1) and w < len(word2):
            res = res + word1[w] + word2[w]
            w += 1

        if w < len(word1):
            res = res + word1[w:len(word1)]
        
        
        if w < len(word2):
            res = res + word2[w:len(word2)]

        return res