import heapq

class Solution:
    def findScore(self, nums: list[int]) -> int:
        h = []
        for i, n in enumerate(nums):
            heapq.heappush(h, (n, i))
        
        seen = set()
        res = 0
        while h:
            n, i = heapq.heappop(h)
            if i not in seen:
                res += n
                seen.add(i-1)
                seen.add(i)
                seen.add(i+1)
        return res