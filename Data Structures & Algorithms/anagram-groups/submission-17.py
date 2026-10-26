class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        '''
        need to return res arr
        analyze each string 
        defaultdict
        '''
        ans = []
        anagram = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            anagram[tuple(count)].append(s)
        return list(anagram.values())