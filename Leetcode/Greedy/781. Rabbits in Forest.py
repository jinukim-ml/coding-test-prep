from collections import Counter

class Solution:
    def numRabbits(self, answers: list[int]) -> int:
        freq = Counter(answers)
        res = 0
        for k, v in freq.items():
            r, q = divmod(v, k+1)
            res += r*(k+1)
            if q:
                res += k+1
        return res