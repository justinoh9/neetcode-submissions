class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # can use sort for each string to check if its an anagram
        groups = {}
        for word in strs:
            key = ''.join(sorted(word))

            if key not in groups:
                groups[key] = []
            #otherwise add the unsorted word to its proper group
            groups[key].append(word)
        return list(groups.values())
    