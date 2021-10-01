class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        b=[]
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]<nums[j]:
                    c=abs(nums[i]-nums[j])
                    b.append(c)
        return max(b) if len(b)>=1 else -1
        