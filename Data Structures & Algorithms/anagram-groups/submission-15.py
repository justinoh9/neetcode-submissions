class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # strs array, return list of lists

        

        # get freq of each char for each word

        freq = defaultdict(list)

        for s in strs:
            # in word

            count = [0] * 26

            for c in s:
                count[ord(c) - ord('a')] += 1

            freq[tuple(count)].append(s)
        
        return list(freq.values())