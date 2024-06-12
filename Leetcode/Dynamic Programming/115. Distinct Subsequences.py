class Solution: # Bottom-up solution
    def numDistinct(self, s: str, t: str) -> int:
        dp = [[0 for j in range(len(t)+1)] for i in range(len(s)+1)]

        for i in range(len(s)+1):
            dp[i][len(t)] = 1
        for j in range(len(t)):
            dp[len(s)][j] = 0

        for i in range(len(s)-1, -1, -1):
            for j in range(len(t)-1, -1, -1):
                if s[i] == t[j]:
                    dp[i][j] = dp[i+1][j+1] + dp[i+1][j]
                else:
                    dp[i][j] = dp[i+1][j]
        return dp[0][0]

class Solution: # Top-down solution
    def numDistinct(self, s: str, t: str) -> int:
        dp = {}
        def dfs(i, j):
            if j == len(t):
                return 1
            if len(s) - i < len(t) - j:
                return 0
            if (i,j) in dp:
                return dp[(i,j)]

            if s[i] == t[j]:
                dp[(i,j)] = dfs(i+1, j+1) + dfs(i+1, j)
            else:
                dp[(i,j)] = dfs(i+1, j)
            
            return dp[(i,j)]
        
        return dfs(0, 0)