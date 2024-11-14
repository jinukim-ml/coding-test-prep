from math import ceil

class Solution:
    def minimizedMaximum(self, n: int, quantities: list[int]) -> int:
        l, r = 1, max(quantities)
        while l < r:
            mid = (l + r) // 2
            ver = self.verify(n, mid, quantities)
            if ver:
                r = mid
            else:
                l = mid + 1
        return l
    
    def verify(self, n: int, val: int, quantities: list[int]) -> int:
        res = 0
        for q in quantities:
            res += ceil(q / val)
        return res <= n