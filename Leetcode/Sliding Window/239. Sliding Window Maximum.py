import heapq
class Solution: # O(n log n)
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        h = []
        res = []
        for i in range(len(nums)):
            heapq.heappush(h, (-nums[i], i))
            if i >= k-1:
                while h and h[0][1] < i-k+1:
                    heapq.heappop(h)
                res.append(-h[0][0])
        return res

from collections import deque
class Solution: # O(n)
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        dq = deque()
        res = []
        l = 0
        for r in range(len(nums)):
            while dq and nums[dq[-1]] < nums[r]:
                dq.pop()
            dq.append(r)
            if l > dq[0]:
                dq.popleft()
            if r >= k-1:
                res.append(nums[dq[0]])
                l += 1
        return res