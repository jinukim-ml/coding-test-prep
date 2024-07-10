from typing import List

class Solution:
    def minOperations(self, logs: List[str]) -> int:
        ans = 0
        for log in logs:
            if log[-1] == '/' and log[0] != '.':
                ans += 1
            elif log == '../' and ans > 0:
                ans -= 1
        return ans