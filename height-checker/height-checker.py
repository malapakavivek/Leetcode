class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        c=0
        a=sorted(heights)
        for i in range(len(heights)):
            if heights[i]!=a[i]:
                c+=1
        return(c)
                

        