class Solution: # brute force solution
    def minimumSumSubarray(self, nums: list[int], l: int, r: int) -> int:
        ans = float('inf')
        for wsize in range(l, r+1):
            window = 0
            left = 0
            for right in range(len(nums)):
                window += nums[right]
                if right - left + 1 == wsize:
                    if window > 0:
                        ans = min(ans, window)
                    window -= nums[left]
                    left += 1
        if ans == float('inf'):
            return -1
        else:
            return ans