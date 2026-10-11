class Solution:
    def isValid(self, s: str) -> bool:
        prio = ['0']
        res = ['0']
        for i in range(len(s)):

            # if prio is empty at first
            if (s[i] == "[") or (s[i] == "(") or (s[i] == "{"):
                prio.append(s[i])
            elif (prio[-1] == '0') and (s[i] == "]" or s[i] == ")" or s[i] == "}"):
                return False
            elif (prio[-1] != "[" and s[i] == "]") or (prio[-1] != "(" and s[i] == ")") or (prio[-1] != "{" and s[i] == "}"):
                return False
            elif (prio[-1] == "[" and s[i] == "]") or (prio[-1] == "(" and s[i] == ")") or (prio[-1] == "{" and s[i] == "}"):
                prio.pop()
        
        return prio == res