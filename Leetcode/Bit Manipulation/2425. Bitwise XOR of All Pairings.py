class Solution:
    def xorAllNums(self, nums1: list[int], nums2: list[int]) -> int:
        first = 0
        if len(nums2)&1: # odd length
            for n in nums1:
                first ^= n
        second = 0
        if len(nums1)&1: # odd length
            for n in nums2:
                second ^= n
        return first ^ second