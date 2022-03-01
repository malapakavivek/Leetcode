class Solution:
    def countBits(self, n: int) -> List[int]:
        b=[]
        for i in range(n+1):
            a=bin(i)
            c=a.count("1")
            b.append(c)
        return b 