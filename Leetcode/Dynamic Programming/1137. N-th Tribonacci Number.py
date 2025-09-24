class Solution:
    def tribonacci(self, n: int) -> int:
        if n < 3:
            if n == 0:
                return 0
            else:
                return 1
        else:
            dp = [0] * (n+1)
            dp[1], dp[2] = 1, 1
            for i in range(3, n+1):
                dp[i] = dp[i-3] + dp[i-2] + dp[i-1]
            return dp[n]

class Solution: # space complexity O(1)
    def tribonacci(self, n: int) -> int:
        if n < 3:
            if n == 0:
                return 0
            else:
                return 1
        prev3, prev2, prev = 0, 1, 1
        res = 0
        for _ in range(3, n+1):
            res = prev3 + prev2 + prev
            prev3 = prev2
            prev2 = prev
            prev = res
        return res