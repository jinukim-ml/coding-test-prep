class Solution:
    def maximumDifference(self, nums: list[int]) -> int:
        res = -1
        maximum = 0
        for i in range(len(nums)-1, -1, -1):
            if nums[i] >= maximum:
                maximum = nums[i]
            else:
                res = max(res, maximum-nums[i])
        return res