class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        q, _ = divmod(n, m)
        num2 = (q * (m + q*m))//2
        return (n*(n+1))//2 - 2*num2