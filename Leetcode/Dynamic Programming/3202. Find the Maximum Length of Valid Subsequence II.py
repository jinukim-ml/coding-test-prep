class Solution:
    def maximumLength(self, nums: list[int], k: int) -> int:
        n = len(nums)
        res = 0
        dp = [[0 for _ in range(k)] for _ in range(k)]
        for i in range(n):
            r = nums[i]%k
            for prev in range(k):
                dp[prev][r] = dp[r][prev]+1 # previous sequence length
                res = max(res, dp[prev][r])
        return res