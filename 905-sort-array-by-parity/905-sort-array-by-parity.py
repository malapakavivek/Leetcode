class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        a=0
        for i in range(len(nums)):
            if nums[i]%2==0:
                nums[a],nums[i]=nums[i],nums[a]
                a+=1
        return nums
                
        