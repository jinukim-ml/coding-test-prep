class Solution:
    def longestSubarray(self, nums: list[int]) -> int:
        zeros = 0
        l, res = 0, 0
        for r in range(len(nums)):
            if nums[r] == 0:
                zeros += 1
            while zeros > 1:
                if nums[l] == 0:
                    zeros -= 1
                l += 1
            res = max(res, r-l)
        return res