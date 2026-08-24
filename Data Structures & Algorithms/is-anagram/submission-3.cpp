class Solution {
public:
    bool isAnagram(string s, string t) {
        /*
            initial thought process

            bool function
            2 strings
            if both strings aren't the same length, return false
            add characters to one set, then 
        */
        // set<char> hashset;
        // if (s.size() != t.size()){
        //     return false;
        // }
        // for (size_t i = 0; i < s.length(); i++) {
        //     hashset.insert(s[i]);
        // }
        // for (size_t j = 0; j < t.length(); j++) {
        //     if (hashset.count(t[j]) == false){
        //         return false; 
        //     } 
        // }

        // return true;
        

        //attempt 2
        sort(s.begin(), s.end());
        sort(t.begin(), t.end());
        return s == t;


    
    }
};
