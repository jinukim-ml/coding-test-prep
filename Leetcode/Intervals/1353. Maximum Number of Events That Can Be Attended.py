import heapq

class Solution:
    def maxEvents(self, events: list[list[int]]) -> int:
        events.sort(key=lambda x: x[0])
        i, res = 0, 0
        day = events[0][0]
        h = []
        while i < len(events) or h:
            while i < len(events) and events[i][0] == day:
                heapq.heappush(h, events[i][1])
                i += 1
            while h and h[0] < day:
                heapq.heappop(h)
            if h:
                heapq.heappop(h)
                res += 1
            day += 1
            if not h and i < len(events):
                day = max(day, events[i][0])
        return res