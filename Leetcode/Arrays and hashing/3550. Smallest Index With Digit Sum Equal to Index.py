class Solution:
    def smallestIndex(self, nums: list[int]) -> int:
        for i in range(len(nums)):
            n = nums[i]
            digitsum = 0
            while n:
                n, r = divmod(n, 10)
                digitsum += r
            if digitsum == i:
                return i
        return -1