class Solution:
    def maxDepth(self, s: str) -> int:
        lefts, rights = 0, 0
        res = 0
        for ch in s:
            if ch == '(':
               lefts += 1
            elif ch == ')':
                rights += 1
            res = max(res, lefts-rights)
        return res