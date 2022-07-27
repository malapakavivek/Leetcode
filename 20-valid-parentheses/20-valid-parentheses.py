class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        look={")":"(","}":"{","]":"["}
        if len(s)%2!=0:
            return False
        
        for i in s:
            if i in look.values():
                stack.append(i)
            elif stack and look[i] is stack[-1]:
                stack.pop()
            else:
                return False
            
        return stack==[]
