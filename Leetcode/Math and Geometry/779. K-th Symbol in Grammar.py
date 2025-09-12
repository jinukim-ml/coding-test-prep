# time complexity: O(n)
class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if n == 1:
            return 0
        if 1 <= k <= 1<<(n-2): # left half
            return self.kthGrammar(n-1, k)
        else:
            return self.kthGrammar(n-1, k-(1<<(n-2)))^1

# time complexity: O(log n)
class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        return bin(k-1).count('1')&1