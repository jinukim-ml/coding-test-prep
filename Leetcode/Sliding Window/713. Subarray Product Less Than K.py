class Solution:
    def numSubarrayProductLessThanK(self, nums: list[int], k: int) -> int:
        win_pro, win_len = 1, 0
        l = 0
        res = 0
        for r in range(len(nums)):
            win_pro *= nums[r]
            win_len += 1
            while win_len and win_pro >= k:
                win_pro //= nums[l]
                win_len -= 1
                l += 1
            res += win_len
        return res