from collections import Counter

class Solution:
    def longestBalanced(self, s: str) -> int:
        res = 1
        for l in range(len(s)):
            freq = Counter()
            for r in range(l, len(s)):
                freq[s[r]] += 1
                if len(set(freq.values())) == 1:
                    res = max(res, r-l+1)
        return res