class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # the idea is that we need to create sublists for words that are anagrams
        # one idea is that we can use a dictionary
        # the key of the dict can be a list of the count of characters of each word, while the value is the group
        res = defaultdict(list) # mapping charCount to list of Anagrams
        # first we should iterate the list of strings
        for word in strs:
            # then we need to sort the words by their char count
            count = [0] * 26 # a ... z

            for char in word:
                count[ord(char) - ord("a")] += 1 #increment by 1 b/c counting num of char
            res[tuple(count)].append(word)
        
        return list(res.values())