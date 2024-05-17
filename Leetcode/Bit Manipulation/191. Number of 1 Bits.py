class Solution: # intended solution
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n:
            n &= n - 1
            res += 1
        return res

class Solution: # pythonian solution
    def hammingWeight(self, n: int) -> int:
        n = bin(n)

        ans = 0
        for i in range(2, len(n)):
            if n[i] == '1':
                ans += 1
        return ans

class Solution: # another pythonian solution
    def hammingWeight(self, n: int) -> int:
        return n.bit_count()