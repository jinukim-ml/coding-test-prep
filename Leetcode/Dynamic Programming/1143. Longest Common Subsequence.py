class Solution: # iteration (bottom-up approach)
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0] * (len(text2)+1) for _ in range(len(text1)+1)]

        for r in range(len(text1)-1, -1, -1):
            for c in range(len(text2)-1, -1, -1):
                if text1[r] == text2[c]:
                    dp[r][c] = 1 + dp[r+1][c+1]
                else:
                    dp[r][c] = max(dp[r+1][c], dp[r][c+1])
        
        return dp[0][0]

class Solution: # recursion + memoization (top-down approach)
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        self.m, self.n = len(text1), len(text2)
        self.t1, self.t2 = text1, text2
        self.dp = [[-1] * len(text2) for _ in range(len(text1))]

        return self.recur(0, 0)

    def recur(self, i: int, j: int) -> int:
        if i == self.m or j == self.n:
            return 0

        if self.dp[i][j] == -1:
            if self.t1[i] == self.t2[j]:
                self.dp[i][j] = 1 + self.recur(i+1, j+1)
            else:
                self.dp[i][j] = max(self.recur(i+1, j), self.recur(i, j+1))
        return self.dp[i][j]