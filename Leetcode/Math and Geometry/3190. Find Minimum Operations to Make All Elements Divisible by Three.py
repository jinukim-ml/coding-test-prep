class Solution:
    def minimumOperations(self, nums: list[int]) -> int:
        res = 0
        for n in nums:
            if n%3:
                res += 1
        return res