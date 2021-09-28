class Solution:
    def findLucky(self, arr: List[int]) -> int:
        a=[]
        for i in arr:
            if arr.count(i)==i:
                a.append(i)
        return(max(a)) if len(a)>=1 else -1