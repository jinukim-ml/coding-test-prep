class Solution: # sorting. O(n log n)
    def buyChoco(self, prices: list[int], money: int) -> int:
        prices.sort()
        return money - prices[0] - prices[1] if prices[0] + prices[1] <= money else money

class Solution: # greedy w/ O(n)
    def buyChoco(self, prices: list[int], money: int) -> int:
        m1 = m2 = float('inf')
        for p in prices:
            if p < m1:
                m1 = p
            elif p < m2:
                m2 = p
        leftover = money - m1 - m2
        if leftover >= 0:
            return leftover
        else:
            return money