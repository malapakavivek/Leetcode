class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        a=[]
        for i in nums:
            b=i**2
            a.append(b)
        a.sort()
        return a
        