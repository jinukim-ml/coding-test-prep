class Solution: # w/ loop
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        while n > 1:
            n, r = divmod(n, 3)
            if r:
                return False
        return True

from math import log, ceil
class Solution: # w/o loop
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        l = log(n, 3)
        return n == 3**ceil(l)