class Solution:
    def maxOperations(self, s: str) -> int:
        i, ones, res = 0, 0, 0
        while i < len(s):
            if s[i] == '0':
                while i+1 < len(s) and s[i+1] == '0':
                    i += 1
                res += ones
            else:
                ones += 1
            i += 1
        return res