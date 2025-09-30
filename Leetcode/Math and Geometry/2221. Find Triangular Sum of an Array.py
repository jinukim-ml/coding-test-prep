class Solution: # simple brute force
    def triangularSum(self, nums: list[int]) -> int:
        while len(nums) > 1:
            newnums = []
            for i in range(len(nums)-1):
                newnums.append((nums[i] + nums[i+1])%10)
            nums = newnums
        return nums[0]

from math import comb

class Solution: # pascal's triangle
    def triangularSum(self, nums: list[int]) -> int:
        n = len(nums)
        total = 0
        for i in range(n):
            total += nums[i] * comb(n-1,i)
        return total%10