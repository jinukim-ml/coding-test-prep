class Solution:
    def minSum(self, nums1: list[int], nums2: list[int]) -> int:
        nums1_zeros = 0
        nums1_total = 0
        for n in nums1:
            nums1_total += n
            if n == 0:
                nums1_zeros += 1
        
        nums2_zeros = 0
        nums2_total = 0
        for n in nums2:
            nums2_total += n
            if n == 0:
                nums2_zeros += 1
        
        if nums1_zeros == 0 and nums1_total < nums2_total + nums2_zeros:
            return -1
        if nums2_zeros == 0 and nums1_total + nums1_zeros > nums2_total:
            return -1
        return max(nums1_total + nums1_zeros, nums2_total + nums2_zeros)