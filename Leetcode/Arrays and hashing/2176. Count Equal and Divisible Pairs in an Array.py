from collections import defaultdict

class Solution:
    def countPairs(self, nums: list[int], k: int) -> int:
        freq = defaultdict(list)
        res = 0
        for i, n in enumerate(nums):
            for j in freq[n]:
                if (i*j)%k == 0:
                    res += 1
            freq[n].append(i)
        return res