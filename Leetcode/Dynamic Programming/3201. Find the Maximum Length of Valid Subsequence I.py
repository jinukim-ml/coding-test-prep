class Solution:
    def maximumLength(self, nums: list[int]) -> int:
        n = len(nums)
        odd, even, alternating = 0, 0, 0
        bit = nums[0]%2
        for i in range(n):
            if nums[i]%2 == bit:
                alternating += 1
                bit ^= 1
            if nums[i]%2:
                odd += 1
            else:
                even += 1
        return max(odd, even, alternating)