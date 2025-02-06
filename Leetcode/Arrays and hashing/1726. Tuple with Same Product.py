from collections import defaultdict

class Solution:
    def tupleSameProduct(self, nums: list[int]) -> int:
        freq = defaultdict(int)
        res = 0
        for i in range(len(nums)):
            for j in range(i):
                prod = nums[i] * nums[j]
                res += freq[prod] * 8
                freq[prod] += 1
        return res