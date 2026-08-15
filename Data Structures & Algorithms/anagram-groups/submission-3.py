class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        #thoughts go through the list, checking if each word has anagrams
        # if it doesnt, itll create a list with only istelf, and append it to a larger list
        #if it does, create a list with itself along with the others, while removing from the main list
        #first make checking feature
        #probably want to use a dict
        groups = {}
        for word in strs:
            key = ''.join(sorted(word))

            if key not in groups:
                groups[key] = []

            groups[key].append(word)
        return list(groups.values())