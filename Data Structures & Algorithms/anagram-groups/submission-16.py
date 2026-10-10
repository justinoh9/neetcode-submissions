class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # sorting buckets

        # need a dict to count freq

        freqVal = defaultdict(list)

        for s in strs:

            count = [0] * 26

            for c in s:
                count[ord(c) - ord('a')] += 1
            
            freqVal[tuple(count)].append(s)

        return list(freqVal.values())