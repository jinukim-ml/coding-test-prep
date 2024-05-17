from typing import List

class Solution: # dp solution
    def countBits(self, n: int) -> List[int]:
        dp = [0] * (n + 1)
        offset = 1

        for i in range(1, n + 1):
            if offset * 2 == i:
                offset = i
            dp[i] = 1 + dp[i - offset]
        return dp

class Solution: # pythonian solution
    def countBits(self, n: int) -> List[int]:
        return [i.bit_count() for i in range(n+1)]