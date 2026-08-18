class Solution:
    def isValid(self, s: str) -> bool:
        # idea is use a stack here
        # whenever you see an opening character, you push that to highest priority, so top of stack
        prioStack = []
        for i in range(len(s)):
            # case 1: if its an opening bracket, send to top of stack
            if s[i] == "[" or s[i] == "{" or s[i] == "(":
                prioStack.append(s[i])
            # case 2: if the stack is empty after case 1, we can invalidate the entire string. so return false
            elif not prioStack:
                return False
            # case 3: if the stack is not empty after case 1 and there is a closing bracket with a matching opening bracket remaining in the stack
            #         but it wasn't the most recent opening bracket
            elif (s[i] == "]" and prioStack[-1] != "[") or (s[i] == "}" and prioStack[-1] != "{") or (s[i] == ")" and prioStack[-1] != "("):
                return False
            # case 4: if the top of stack is an opening bracket, and current element is a closing bracket that matches, pop out of stack
            elif (s[i] == "]" and prioStack[-1] == "[") or (s[i] == "}" and prioStack[-1] == "{") or (s[i] == ")" and prioStack[-1] == "("):
                prioStack.pop()
        # returns true only if stack is empty
        return prioStack == []
            