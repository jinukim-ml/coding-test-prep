class Solution:
    def minimumSteps(self, s: str) -> int:
        ans, zeros = 0, 0
        for r in range(len(s)-1, -1, -1):
            if s[r] == '0':
                zeros += 1
            else:
                ans += zeros
        return ans