class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        # iterate through the array
        # then iterate through each string
        # add letters of string to a dict
        #   where the key is the letter and the value is the freq
        for i in range(len(strs)):
            sortedString = ''.join(sorted(strs[i]))
            res[sortedString].append(strs[i])
        return list(res.values())
