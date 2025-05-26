from collections import Counter

class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
        cnt = Counter(nums)
        res = []
        for k, v in cnt.items():
            if v > len(nums)//3:
                res.append(k)
        return res