class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # create a dictionary where:
        #     key = letter-frequency signature
        #     value = list of words with that signature
        res = defaultdict(list)
        # for each word in strs:
        for s in strs:
        #     create an array of 26 zeros
            count = [0] * 26
        #     for each character in the word:
            for c in s:
        #         figure out which index 0-25 that character belongs to
        #         increment that position in the array
                count[ord(c) - ord('a')] += 1
        #     convert the 26-number array into something usable as a dictionary key

        #     add the current word to the list stored at that key
            res[tuple(count)].append(s)
        # return all the dictionary's values as a list
        return list(res.values())