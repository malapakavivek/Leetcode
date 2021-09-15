class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        txt=s.split()
        a=txt[-1]
        c=0
        for i in a:
            c+=1
        return c
        