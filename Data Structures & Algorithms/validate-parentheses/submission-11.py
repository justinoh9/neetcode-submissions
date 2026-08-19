class Solution:
    def isValid(self, s: str) -> bool:
        # every open bracket is closed by same type of closed bracket
        # open brackets are closed in correct order
        # every close bracket has corresponding open bracket of same type

        # use a stack here
        prio = ["l"]

        for i in range(len(s)):
            # first case: if bracket is even an open bracket or not
            if s[i] == "(" or s[i] == "[" or s[i] == "{":
                prio.append(s[i])
            
            # second case: if bracket is a closing bracket but there isn't a matching opening bracket in the stack
            elif (s[i] == ")" and prio[-1] != "(") or (s[i] == "]" and prio[-1] != "[") or (s[i] == "}" and prio[-1] != "{"):
                return False
            # third case: happy case
            elif (s[i] == ")" and prio[-1] == "(") or (s[i] == "]" and prio[-1] == "[") or (s[i] == "}" and prio[-1] == "{"):
                prio.pop()
        return prio == ["l"]