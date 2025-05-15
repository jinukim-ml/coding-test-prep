from collections import Counter

class Solution:
    def numIdenticalPairs(self, nums: list[int]) -> int:
        cnt = Counter(nums)
        res = 0
        for k, v in cnt.items():
            res += (v-1)*v//2
        return res