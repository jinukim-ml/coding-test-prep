from collections import Counter

class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        s1_odds, s1_evens = Counter(), Counter()
        s2_odds, s2_evens = Counter(), Counter()
        n = len(s1)
        for i in range(n):
            if i%2:
                s1_odds[s1[i]] += 1
                s2_odds[s2[i]] += 1
            else:
                s1_evens[s1[i]] += 1
                s2_evens[s2[i]] += 1

        if s1_odds != s2_odds or s1_evens != s2_evens:
            return False
        return True