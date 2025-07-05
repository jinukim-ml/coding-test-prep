from collections import Counter

class Solution:
    def findLucky(self, arr: list[int]) -> int:
        freq = Counter(arr)
        res = -1
        for k, v in freq.items():
            if k == v:
                res = max(res, k)
        if res != -1:
            return res
        else:
            return -1