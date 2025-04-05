class Solution: # backtracking + copy
    def combine(self, n: int, k: int) -> list[list[int]]:
        res = []
        def backtrack(i: int, arr: list[int]) -> None:
            if len(arr) == k:
                res.append(arr[:])
                return
            if i == n+1:
                if len(arr) == k:
                    res.append(arr[:])
                return
            arr.append(i)
            backtrack(i+1, arr)
            arr.pop()
            backtrack(i+1, arr)
        backtrack(1, [])
        return res

from itertools import combinations

class Solution: # this is faster because there is no O(k) copy operation
    def combine(self, n: int, k: int) -> list[list[int]]:
        nums = []
        for i in range(1, n + 1):
            nums.append(i)
        res = []
        for comb in combinations(nums, k):
            res.append(comb)
        return res