class Solution:
    def maxCount(self, banned: list[int], n: int, maxSum: int) -> int:
        banned = set(banned)
        res = 0
        total = 0
        curr = 1
        for curr in range(1, n+1):
            if curr not in banned and total + curr <= maxSum:
                total += curr
                res += 1
        return res