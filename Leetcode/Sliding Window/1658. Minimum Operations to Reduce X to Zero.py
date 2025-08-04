class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        n = len(nums)
        l = 0
        winsum, winlen = 0, -1
        x = sum(nums) - x
        for r in range(n):
            winsum += nums[r]
            while winsum > x and l <= r:
                winsum -= nums[l]
                l += 1
            if winsum == x:
                winlen = max(winlen, r-l+1)
        if winlen == -1:
            return -1
        else:
            return n - winlen