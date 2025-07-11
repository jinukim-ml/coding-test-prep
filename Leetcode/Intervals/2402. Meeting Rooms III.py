import heapq

class Solution:
    def mostBooked(self, n: int, meetings: list[list[int]]) -> int:
        meetings.sort(key=lambda x: x[0])
        counts = [0 for _ in range(n)]
        available = [i for i in range(n)]
        in_use = []
        for i in range(len(meetings)):
            while in_use and in_use[0][0] <= meetings[i][0]:
                _, room = heapq.heappop(in_use)
                heapq.heappush(available, room)
            if available:
                room = heapq.heappop(available)
                heapq.heappush(in_use, (meetings[i][1], room))
            else:
                end_time, room = heapq.heappop(in_use)
                diff = end_time - meetings[i][0]
                end_time = meetings[i][1] + diff
                heapq.heappush(in_use, (end_time, room))
            counts[room] += 1
        
        res, val = 0, 0
        for room in range(n):
            if counts[room] > val:
                val = counts[room]
                res = room
        return res