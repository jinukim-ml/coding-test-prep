class Solution:
    def arrangeCoins(self, n: int) -> int:
        l, r = 1, n
        res = 0
        while l <= r:
            mid = (l+r)//2
            used_coins = ((mid+1)*mid)//2
            if used_coins <= n:
                res = max(res, mid)
                l = mid+1
            else:
                r = mid-1
        return res