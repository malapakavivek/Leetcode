class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        b=sorted(nums)
        c=b[0]*b[1]*b[-1]
        d=b[0]*b[1]*b[2]
        e=b[-3]*b[-2]*b[-1]
        return(max(c,d,e))
    
        