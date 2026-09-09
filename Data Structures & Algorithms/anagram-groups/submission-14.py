class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        wordFreq = defaultdict(list)

        # populate wordFreq

        for s in strs:
            # use a list as key
            count = [0] * 26

            for c in s:
                count[ord(c) - ord('a')] += 1
            
            wordFreq[tuple(count)].append(s)

        return list(wordFreq.values())