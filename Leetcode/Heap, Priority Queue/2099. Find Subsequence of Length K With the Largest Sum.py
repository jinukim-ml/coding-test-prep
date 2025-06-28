import heapq

class Solution:
    def maxSubsequence(self, nums: list[int], k: int) -> list[int]:
        h = []
        total = 0
        for i, n in enumerate(nums):
            if len(h) < k:
                heapq.heappush(h, (n, i))
                total += n
            else:
                if n > h[0][0]:
                    heapq.heappop(h)
                    heapq.heappush(h, (n,i))
        
        temp = []
        while h:
            n, i = heapq.heappop(h)
            heapq.heappush(temp, (i,n))
        res = []
        while temp:
            _, n = heapq.heappop(temp)
            res.append(n)
        return res