class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        a=0
        b=1
        for i in str(n):
            a+=int(i)
            b*=int(i)
        return b-a
        