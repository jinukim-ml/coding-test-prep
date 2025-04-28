class Solution:
    def countSubarrays(self, nums: list[int], k: int) -> int:
        l = 0
        win_sum, win_len = 0, 0
        res = 0
        for r in range(len(nums)):
            win_sum += nums[r]
            win_len += 1
            while win_sum * win_len >= k:
                win_sum -= nums[l]
                win_len -= 1
                l += 1
            res += win_len
        return res