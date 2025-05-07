import heapq

class Solution:
    def minTimeToReach(self, moveTime: list[list[int]]) -> int:
        n, m = len(moveTime), len(moveTime[0])
        mintime = [[float('inf') for _ in range(m)] for _ in range(n)]
        mintime[0][0] = 0
        h = [(0,0,0)]
        directions = [(-1,0), (0,1), (1,0), (0,-1)]
        while h:
            t, r, c = heapq.heappop(h)
            if r == n-1 and c == m-1:
                return t
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < m:
                    new_time = max(moveTime[nr][nc]+1, t+1)
                    if new_time < mintime[nr][nc]:
                        mintime[nr][nc] = new_time
                        heapq.heappush(h, (new_time, nr, nc))