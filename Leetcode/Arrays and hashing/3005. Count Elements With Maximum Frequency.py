from collections import Counter

class Solution:
    def maxFrequencyElements(self, nums: list[int]) -> int:
        cnt = Counter(nums)
        maxfreq = max(cnt.values())
        res = 0
        for k, v in cnt.items():
            if v == maxfreq:
                res += v
        return res