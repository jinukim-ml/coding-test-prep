class Solution:
    def maxAscendingSum(self, nums: list[int]) -> int:
        prev = 0
        maxsum = 0
        localsum = 0
        for r in range(len(nums)):
            if nums[r] > prev:
                localsum += nums[r]
            else:
                localsum = nums[r]
            maxsum = max(maxsum, localsum)
            prev = nums[r]
        return maxsum