from collections import defaultdict

class Solution:
    def lenLongestFibSubseq(self, arr: list[int]) -> int:
        dp = defaultdict(int)
        indices = {val: i for i, val in enumerate(arr)}
        res = 0

        def fib(f0: int, f1: int) -> int:
            curr = f0 + f1
            if curr not in indices:
                return 0
            if (f0, f1) in dp:
                return dp[(f0, f1)]
            length = fib(f1, curr)
            dp[(f0, f1)] += length
            return dp[(f0, f1)] + 1

        for i in range(len(arr)-2):
            for j in range(i+1, len(arr)):
                length = fib(arr[i], arr[j])
                if length:
                    res = max(res, length+2)
        return res

class Solution: # More optimized solution. Source: leetcode
    def lenLongestFibSubseq(self, arr: list[int]) -> int:
        dp = {}
        res = 0
        for i, num in enumerate(arr):
            dp[num] = defaultdict(lambda: 2)
            for j in range(i-1, -1, -1):
                f1 = arr[j]
                f0 = num - f1
                if f0 >= f1:
                    break
                if f0 not in dp:
                    continue
                dp[num][f1] = dp[f1][f0] + 1
                res = max(res, dp[num][f1])
        return res