class Solution:
    def longestSubsequence(self, nums: list[int]) -> int:
        if sum(nums) == 0:
            return 0
        val = 0
        for n in nums:
           val ^= n
        return len(nums) if val else len(nums)-1