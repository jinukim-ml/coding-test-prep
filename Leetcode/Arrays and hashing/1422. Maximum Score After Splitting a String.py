class Solution:
    def maxScore(self, s: str) -> int:
        left, right = 0, s.count('1')
        res = 0
        for i in range(len(s)-1):
            if s[i] == '0':
                left += 1
            else:
                right -= 1
            res = max(res, left + right)
        return res