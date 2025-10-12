from collections import Counter

class Solution:
    def deleteAndEarn(self, nums: list[int]) -> int:
        freq = Counter(nums)
        nums = sorted(list(freq.keys()))
        n = len(nums)
        dp = [0 for _ in range(n+1)]
        for i in reversed(range(n)):
            take = nums[i] * freq[nums[i]]
            if i+1 < n and nums[i+1] == nums[i]+1:
                take += dp[i+2]
            else:
                take += dp[i+1]
            dp[i] = max(take, dp[i+1])
        return dp[0]