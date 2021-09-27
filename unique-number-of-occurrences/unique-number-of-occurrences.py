class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        d={}
        for i in arr:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        a=[]
        for k,v in d.items():
            if v not in a:
                a.append(v)
            else:
                return False
        return True