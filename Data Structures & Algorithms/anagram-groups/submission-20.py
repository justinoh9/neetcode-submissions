class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        groups = {}
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            
            if tuple(count) not in groups:
                groups[tuple(count)] = [s]
            else:
                groups[tuple(count)].append(s)
        res = list(groups.values())
        return res