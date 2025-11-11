class Solution:
    def findMaxForm(self, strs: list[str], m: int, n: int) -> int:
        for i in range(len(strs)):
            zeros = strs[i].count('0')
            ones = len(strs[i]) - zeros
            strs[i] = (zeros, ones)

        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
        for freq in strs:
            zeros, ones = freq[0], freq[1]
            for i in reversed(range(zeros, m+1)):
                for j in reversed(range(ones, n+1)):
                    dp[i][j] = max(dp[i][j], dp[i-zeros][j-ones]+1)
        return dp[m][n]