class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        d=collections.defaultdict(int)
        for i,j in paths:
            d[i]+=1
            d[j]+=0
        for x in d:
            if d[x]==0:
                return x
        return ""