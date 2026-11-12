class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        wordFreq = {}

        for s in strs:
            count = [0] * 26

            for c in s:
                count[ord(c) - ord('a')] += 1
            if tuple(count) not in wordFreq:
                wordFreq[tuple(count)] = wordFreq.get(tuple(count), [s])
            else:
                wordFreq[tuple(count)].append(s)
        ans = list(wordFreq.values())

        return ans