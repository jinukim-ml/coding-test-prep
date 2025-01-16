class Solution:
    def xorAllNums(self, nums1: list[int], nums2: list[int]) -> int:
        res = 0
        if len(nums2)&1: # odd length
            for n in nums1:
                res ^= n
        if len(nums1)&1: # odd length
            for n in nums2:
                res ^= n
        return res