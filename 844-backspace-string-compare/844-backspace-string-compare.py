class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack1=[]
        stack2=[]
        for i in s:
            if i.isalpha() or i.isdigit():
                stack1.append(i)
            elif stack1==[] and i=="#":
                continue
            else:
                stack1.pop()
                
        for j in t:
            if j.isalpha() or j.isdigit():
                stack2.append(j)
            elif stack2==[] and j=="#":
                continue
            else:
                stack2.pop()
        if stack1==stack2:
            return True
        
        