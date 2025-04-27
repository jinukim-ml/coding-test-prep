class Solution:
    def countSubarrays(self, nums: list[int]) -> int:
        l = 0
        res = 0
        for r in range(2, len(nums)):
            if r - l + 1 > 3:
                l += 1
            if nums[r] + nums[l] == nums[r-1]/2:
                res += 1
        return res