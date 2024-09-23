class Solution:
    def minExtraChar(self, s: str, dictionary: list[str]) -> int:
        dp = [0] * (len(s) + 1)
        dictionary = set(dictionary)

        for i in range(len(s)-1, -1, -1):
            dp[i] = 1 + dp[i + 1]
            for j in range(i, len(s)):
                curr = s[i:j+1]
                if curr in dictionary:
                    dp[i] = min(dp[i], dp[j+1])
        return dp[0]