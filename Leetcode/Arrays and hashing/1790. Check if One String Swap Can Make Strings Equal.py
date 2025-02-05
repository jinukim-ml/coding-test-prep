from collections import Counter

class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if Counter(s1) != Counter(s2):
            return False
        cnt = 0
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                cnt += 1
        if cnt == 0 or cnt == 2:
            return True
        return False