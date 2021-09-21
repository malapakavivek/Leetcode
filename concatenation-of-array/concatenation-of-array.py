class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        b=[]
        for i in nums:
            b.append(i)
        nums=nums+b
        return nums
        
        