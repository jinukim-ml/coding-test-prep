class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        start = 1
        while start <= n:
            if start == n:
                return True
            else:
                start <<= 1
        return False

class Solution: # no loop solution
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        if n == 1:
            return True
        if bin(n)[-1] == 1 or n.bit_count() > 1:
            return False
        return True