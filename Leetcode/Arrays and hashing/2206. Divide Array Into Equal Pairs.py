from collections import Counter

class Solution:
    def divideArray(self, nums: list[int]) -> bool:
        for k, v in Counter(nums).items():
            if v%2:
                return False
        return True