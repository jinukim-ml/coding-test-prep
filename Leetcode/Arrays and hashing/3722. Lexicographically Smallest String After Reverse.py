class Solution:
    def lexSmallest(self, s: str) -> str:
        res = min(s, s[::-1])
        for k in range(1,len(s)):
            t = s[:k][::-1] + s[k:]
            u = s[:k] + s[k:][::-1]
            res = min(res, t, u)
        return res