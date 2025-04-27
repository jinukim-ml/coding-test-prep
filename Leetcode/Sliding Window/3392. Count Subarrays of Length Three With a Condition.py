class Solution:
    def countSubarrays(self, nums: list[int]) -> int:
        res = 0
        for r in range(2, len(nums)):
            if (nums[r] + nums[r-2])*2 == nums[r-1]:
                res += 1
        return res