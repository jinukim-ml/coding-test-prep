class Solution:
    def shipWithinDays(self, weights: list[int], days: int) -> int:
        l, r = 0, 0
        for n in weights:
            l = max(l, n)
            r += n
        res = r
        
        def is_possible(wcap: int) -> bool:
            d, limit = 1, wcap
            for w in weights:
                if limit - w < 0:
                    d += 1
                    limit = wcap
                    if d > days:
                        return False
                limit -= w
            return True
        
        while l <= r:
            mid = (l+r)//2
            if is_possible(mid):
                res = min(res, mid)
                r = mid-1
            else:
                l = mid+1
        return res