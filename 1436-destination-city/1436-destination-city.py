class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        l=[]
        for i in range (len(paths)):
            if paths[i] not in l:
                l.append(paths[i][0])
        for i, j in paths:
            if j not in l:
                return j
        