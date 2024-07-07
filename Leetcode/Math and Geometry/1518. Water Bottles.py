class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        ans, total = numBottles, numBottles
        while total//numExchange:
            full, empty = divmod(total, numExchange)
            total = full + empty
            ans += full
        return ans