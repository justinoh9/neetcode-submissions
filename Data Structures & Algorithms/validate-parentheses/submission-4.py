class Solution:
    def isValid(self, s: str) -> bool:
        # idea is use a stack here
        # whenever you see an opening character, you push that to highest priority, so top of stack
        prioStack = []
        for i in range(len(s)):
            if s[i] == "[" or s[i] == "{" or s[i] == "(":
                prioStack.append(s[i])
            elif not prioStack:
                return False
            elif (s[i] == "]" and prioStack[-1] != "[") or (s[i] == "}" and prioStack[-1] != "{") or (s[i] == ")" and prioStack[-1] != "("):
                return False
            elif (s[i] == "]" and prioStack[-1] == "[") or (s[i] == "}" and prioStack[-1] == "{") or (s[i] == ")" and prioStack[-1] == "("):
                prioStack.pop()
            
        return prioStack == []
            