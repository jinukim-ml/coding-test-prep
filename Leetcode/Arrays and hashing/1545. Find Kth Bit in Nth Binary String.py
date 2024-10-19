class Solution: # optimized
    def findKthBit(self, n: int, k: int) ->str:
        def helper(n, k):
            if n == 1:
                return '0'
            length = 2 ** n - 1
            mid = 2 ** (n - 1)
            if k == mid:
                return '1'
            elif k < mid:
                return helper(n - 1, k)
            else:
                bit = helper(n - 1, length - k + 1)
                return '1' if bit == '0' else '0'
        return helper(n, k)

class Solution: # brute force
    def findKthBit(self, n: int, k: int) -> str:
        s = ['0']
        for _ in range(n):
            s = s + ['1'] + self.flip(s)[::-1]
        return s[k-1]
    
    def flip(self, s: str) -> str:
        for i, ch in enumerate(s):
            if ch == '0':
                s[i] = '1'
            else:
                s[i] = '0'
        return s