import math

class Solution:
    def replaceNonCoprimes(self, nums: list[int]) -> list[int]:
        stack = []
        for n in nums:
            while stack:
                g = math.gcd(stack[-1],n)
                if g > 1:
                    elem = stack.pop()
                    n *= elem//g
                else:
                    break
            stack.append(n)
        return stack