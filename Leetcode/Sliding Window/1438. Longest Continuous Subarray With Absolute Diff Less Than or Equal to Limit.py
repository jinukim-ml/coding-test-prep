from typing import List
from collections import deque

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        l, ans = 0, 0
        increasing, decreasing = deque(), deque()
        for r, n in enumerate(nums):
            while increasing and n < increasing[-1]:
                increasing.pop()
            increasing.append(n)

            while decreasing and n > decreasing[-1]:
                decreasing.pop()
            decreasing.append(n)

            while decreasing[0] - increasing[0] > limit:
                if nums[l] == decreasing[0]:
                    decreasing.popleft()
                if nums[l] == increasing[0]:
                    increasing.popleft()
                l += 1
            
            ans = max(ans, r - l + 1)
        return ans