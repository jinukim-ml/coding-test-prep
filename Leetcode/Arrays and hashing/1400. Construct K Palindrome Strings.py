from collections import Counter

class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if len(s) < k:
            return False
        cnt = Counter(s)
        odds, evens = 0, 0
        for _, v in cnt.items():
            if v%2 == 1:
                odds += 1
            else:
                evens += 1
        
        if odds > k:
            return False
        else:
            return True