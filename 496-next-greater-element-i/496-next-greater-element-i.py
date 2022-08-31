class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        b=[]
        for i in nums1:
            found=0
            for j in range(nums2.index(i),len(nums2)):
                if nums2[j]>i:
                    b.append(nums2[j])
                    found=1
                    break
            if found==0:
                b.append(-1)
        return b           
            
        