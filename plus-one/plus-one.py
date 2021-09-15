class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits=list(str(digits))
        a=""
        l=[]
        for i in digits:
            if i.isdigit():
                a+=str(i)
        b=int(a)+1
        for i in str(b):
            l.append(i)
        return l 
            
            
        