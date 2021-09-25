class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        a=sorted(nums)
        d=abs(a[0]*a[1])
        e=a[-1]*a[-2]
        return(e-d)