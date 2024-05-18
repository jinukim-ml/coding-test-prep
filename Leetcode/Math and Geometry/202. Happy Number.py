class Solution:
    def isHappy(self, n: int) -> bool:
        rec = {n}
        agg = 0, n
        while n != 1:
            if n//10 > 0:
                agg = 0
                for x in str(n):
                    agg += int(x)**2
            else:
                agg = n ** 2

            if agg in rec:
                return False
            
            rec.add(agg)
            n = agg
            
        return True