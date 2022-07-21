class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        b=sorted(nums)
        c=len(nums)
        for i in range(0,len(b)):
            if i==b[i]:
                continue
            else:
                return i
                break
        if c not in nums:
            return c
        