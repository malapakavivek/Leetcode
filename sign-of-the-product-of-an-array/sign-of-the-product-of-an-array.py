class Solution:
    def arraySign(self, nums: List[int]) -> int:
        mul=prod(nums)
        if mul>0:
            return 1
        elif mul<0:
            return -1
        else:
            return 0
        
        