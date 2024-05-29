class Solution:
    def fib(self, n: int) -> int:
        t2, t1 = 0, 1 # F(n-2), F(n-1)

        if n == 0:
            return t2
        if n == 1:
            return t1

        for _ in range(n-1):
            ans = t1 + t2
            t2, t1 = t1, ans
        return ans