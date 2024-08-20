class Solution:
    def stoneGameII(self, piles: list[int]) -> int:
        l = len(piles)
        dp = [[0 for _ in range(l + 1)] for _ in range(l + 1)]

        suffix = [0 for _ in range(l + 1)]
        for i in range(l-1, -1, -1):
            suffix[i] = suffix[i+1] + piles[i]
        
        for i in range(l+1):
            dp[i][l] = suffix[i]
        
        for i in range(l-1, -1, -1):
            for j in range(l-1, 0, -1):
                for k in range(1, min(2 * j, l-i) + 1):
                    dp[i][j] = max(dp[i][j], suffix[i] - dp[i+k][max(j, k)])
        return dp[0][1]