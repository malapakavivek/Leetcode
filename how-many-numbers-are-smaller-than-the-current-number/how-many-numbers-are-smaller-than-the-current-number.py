class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        x=[]
        s=sorted(nums)
        for i in nums:
            b=s.index(i)
            x.append(b)
        return x
        