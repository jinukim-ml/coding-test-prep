class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        n = len(s)
        current = 0
        res = 0
        for i in range(n-1, -1, -1):
            if s[i] == '0':
                res += 1
            else:
                increment = 1 << (n-1-i)
                if current + increment <= k:
                    current += increment
                    res += 1
        return res