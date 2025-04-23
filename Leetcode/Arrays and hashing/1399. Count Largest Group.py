from collections import defaultdict

class Solution:
    def countLargestGroup(self, n: int) -> int:
        freq = defaultdict(int)
        for i in range(1, n+1):
            total = 0
            for x in str(i):
                total += int(x)
            freq[total] += 1
        largest_size = max(freq.values())
        res = 0
        for k, v in freq.items():
            if v == largest_size:
                res += 1
        return res