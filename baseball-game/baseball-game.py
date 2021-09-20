class Solution:
    def calPoints(self, ops: List[str]) -> int:
        b=[]
        c=0
        for i in ops:
            if i=="D":
                m=int(b[-1])*2
                b.append(m)
            elif i=="C":
                b.pop(-1)
            elif i=="+":
                f=b[-2:] 
                d=sum(f)
                b.append(d)
            else:
                b.append(int(i))
        return(sum(b))