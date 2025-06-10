from collections import Counter

class Solution:
    def maxDifference(self, s: str) -> int:
        odd, even = 0, float('inf')
        for v in Counter(s).values():
            if v%2:
                odd = max(odd, v)
            else:
                even = min(even, v)
        return odd - even