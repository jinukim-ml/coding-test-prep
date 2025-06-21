from collections import Counter

class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        freq = Counter(word)
        arr = freq.values()
        res = len(word)
        for v1 in arr:
            removals = 0
            for v2 in arr:
                if v1 > v2:
                    removals += v2
                elif v2 > v1 + k:
                    removals += v2 - v1 - k
            res = min(res, removals)
        return res