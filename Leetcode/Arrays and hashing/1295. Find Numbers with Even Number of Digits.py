class Solution:
    def findNumbers(self, nums: list[int]) -> int:
        res = 0
        for n in nums:
            if not len(str(n))%2:
                res += 1
        return res