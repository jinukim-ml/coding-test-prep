class Solution:
    def numSubseq(self, nums: list[int], target: int) -> int:
        nums.sort()
        powers = [1]
        for _ in range(len(nums)-1):
            powers.append((2*powers[-1])%(10**9+7))
        l, r = 0, len(nums)-1
        res = 0
        while l <= r:
            if nums[l] + nums[r] <= target:
                res += powers[r-l]
                l += 1
            else:
                r -= 1
        return res%(10**9+7)