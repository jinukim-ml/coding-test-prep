from collections import Counter
from bisect import bisect_left

class Solution:
    def maximumTotalDamage(self, power: list[int]) -> int:
        cnt = Counter(power)
        power = sorted(list(cnt.keys()))
        n = len(power)
        dp = [0 for _ in range(n+1)]
        for i in reversed(range(n)):
            take = power[i] * cnt[power[i]]
            idx = bisect_left(power, power[i]+3)
            if idx < n:
                take += dp[idx]
            dp[i] = max(take, dp[i+1])
        return dp[0]