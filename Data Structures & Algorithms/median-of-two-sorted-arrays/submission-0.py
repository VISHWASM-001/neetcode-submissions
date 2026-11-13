class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        num = nums1 + nums2
        num.sort()

        length = len(num)

        mid = length // 2

        if length%2==0:
            return (num[mid] + num[mid-1]) / 2
        else:
            return num[mid]    

        
        