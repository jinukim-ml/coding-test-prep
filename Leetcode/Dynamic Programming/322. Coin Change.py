from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = [float('inf')] * (amount+1)
        memo[0] = 0

        for c in coins:
            for i in range(amount+1):
                if c <= i:
                    memo[i] = min(memo[i], memo[i-c]+1)
        
        if memo[amount] != float('inf'):
            return memo[amount]
        else:
            return -1