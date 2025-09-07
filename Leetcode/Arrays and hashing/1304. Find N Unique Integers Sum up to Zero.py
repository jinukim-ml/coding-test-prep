class Solution: # solution 1
    def sumZero(self, n: int) -> list[int]:
        res = []
        if n%2:
            res.append(0)
        for i in range(1, n//2+1):
            res.append(i)
            res.append(-i)
        return res

class Solution: # solution 2
    def sumZero(self, n: int) -> list[int]:
        res = [n*(1-n)//2]
        for i in range(1, n):
            res.append(i)
        return res