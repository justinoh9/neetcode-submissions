class Solution:
    def isValid(self, s: str) -> bool:
        prio = []

        # priority stack quesiton i think

        # iirc, 4 cases

        for i in range(len(s)):
            if (s[i] == "(") or (s[i] == "[") or (s[i] == "{"):
                prio.append(s[i])
            elif not prio:
                return False
            elif (s[i] == ")" and prio[-1] != "(") or (s[i] == "]" and prio[-1] != "[") or (s[i] == "}" and prio[-1] != "{"): 
                return False
            elif (s[i] == ")" and prio[-1] == "(") or (s[i] == "]" and prio[-1] == "[") or (s[i] == "}" and prio[-1] == "{"):
                prio.pop()
        return prio == []