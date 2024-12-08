import heapq

class Solution:
    def maxTwoEvents(self, events: list[list[int]]) -> int:
        events.sort(key=lambda item: (item[0], item[1]))
        h = []
        max_val = 0
        res = 0
        for ev in events:
            while h and h[0][0] < ev[0]:
                max_val = max(max_val, h[0][1])
                heapq.heappop(h)
            
            res = max(res, max_val + ev[2])
            heapq.heappush(h, (ev[1], ev[2]))
        return res