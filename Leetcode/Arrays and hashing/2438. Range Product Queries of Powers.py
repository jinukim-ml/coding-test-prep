from collections import deque
from math import floor, log

class Solution:
    def productQueries(self, n: int, queries: list[list[int]]) -> list[int]:
        MOD = 1000000000+7
        powers = deque()
        while n:
            exponent = floor(log(n, 2))
            if exponent:
                x = pow(2, exponent)
                n -= x
                powers.appendleft(x)
            else: # n == 1
                powers.appendleft(1)
                n -= 1
        
        prefix = []
        prod = 1
        for i in range(len(powers)):
            prod *= powers[i]
            prefix.append(prod)
        
        res = []
        for l, r in queries:
            if l:
                val = prefix[r]//prefix[l-1]
            else:
                val = prefix[r]
            res.append(val%MOD)
        return res

class Solution: # bit manipulation
    def productQueries(self, n: int, queries: list[list[int]]) -> list[int]:
        MOD = 1000000000+7
        powers = []
        while n:
            lsb = n & -n
            powers.append(lsb)
            n ^= lsb
        
        prefix = []
        prod = 1
        for i in range(len(powers)):
            prod *= powers[i]
            prefix.append(prod)
        
        res = []
        for l, r in queries:
            if l:
                val = prefix[r]//prefix[l-1]
            else:
                val = prefix[r]
            res.append(val%MOD)
        return res