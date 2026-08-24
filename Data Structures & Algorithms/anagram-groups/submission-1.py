class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #return a list of lists (sublist) 
        # maybe sort strs first
        # take the first word, sort it, thne compare it to all words in list
        # then remove word from strs
        
        res = defaultdict(list);
        for s in strs:
            sortedS = ''.join(sorted(s));
            res[sortedS].append(s);
        return list(res.values());

        