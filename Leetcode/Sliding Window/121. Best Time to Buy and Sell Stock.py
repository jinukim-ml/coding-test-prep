from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mp = 0
        buyon = 0
        for i in range(len(prices)):
            profit = prices[i] - prices[buyon]
            if profit > mp:
                mp = profit
            if prices[buyon] > prices[i]:
                buyon = i
        return mp