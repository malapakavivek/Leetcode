class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        nums1[m:] = nums2[:n] #changes the last m digits from nums1 and replaces it with n digits from nums2
        nums1.sort()