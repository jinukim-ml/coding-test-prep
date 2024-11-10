class Solution:
    def minimumSubarrayLength(self, nums: list[int], k: int) -> int:
        self.bit_cnt = [0] * 32
        win_len = float('inf')
        l, r = 0, 0

        while r < len(nums):
            self.update_bit_cnt(nums[r], 1)
            while l <= r and self.bit_to_num() >= k:
                win_len = min(win_len, r - l + 1)
                self.update_bit_cnt(nums[l], -1)
                l += 1
            r += 1
        
        return -1 if win_len == float('inf') else win_len

    def update_bit_cnt(self, n: int, diff: int) -> None:
        for i in range(32):
            if n & (1 << i):
                self.bit_cnt[i] += diff
    
    def bit_to_num(self) -> int:
        res = 0
        for i in range(32):
            if self.bit_cnt[i]:
                res |= 1 << i
        return res