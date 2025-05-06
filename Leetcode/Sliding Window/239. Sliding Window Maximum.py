import heapq
class Solution:
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