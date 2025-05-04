from collections import defaultdict

class Solution:
    def numEquivDominoPairs(self, dominoes: list[list[int]]) -> int:
        freq = defaultdict(int)
        for a, b in dominoes:
            if a >= b:
                freq[(a,b)] += 1
            else:
                freq[(b,a)] += 1
        res = 0
        for k, v in freq.items():
            if v > 1:
                res += ((v-1)*v)//2
        return res

class Solution: # more streamlined solution
    def numEquivDominoPairs(self, dominoes: list[list[int]]) -> int:
        freq = defaultdict(int)
        res = 0
        for a, b in dominoes:
            if a >= b:
                res += freq[(a,b)]
                freq[(a,b)] += 1
            else:
                res += freq[(b,a)]
                freq[(b,a)] += 1
        return res