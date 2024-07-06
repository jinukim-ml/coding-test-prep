class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        q, r = divmod(time, n-1)

        if q % 2:
            return n - r
        else:
            return r + 1