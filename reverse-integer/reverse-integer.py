class Solution:
    def reverse(self, x: int) -> int:
        rev=0
        if x<0:
            a=-1
            x=-x
        else:
            a=1
        while x:
            rev=(rev*10)+(x%10)
            x=x//10 
        if rev > pow(2, 31):
            return 0
        else: 
            return rev * a
        