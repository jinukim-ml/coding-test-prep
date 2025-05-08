import heapq
from collections import defaultdict

class Solution:
    def minTimeToReach(self, moveTime: list[list[int]]) -> int:
        n, m = len(moveTime), len(moveTime[0])
        mintime = defaultdict(lambda: float('inf'))
        mintime[(0,0)] = 0
        directions = [(-1,0), (0,1), (1,0), (0,-1)]
        h = [(0,0,0,False)]
        while h:
            t, r, c, flag = heapq.heappop(h)
            if r == n-1 and c == m-1:
                return t
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < m:
                    if flag:
                        t_next = max(moveTime[nr][nc]+2, t+2)
                    else:
                        t_next = max(moveTime[nr][nc]+1, t+1)
                    if t_next < mintime[(nr,nc)]:
                        mintime[(nr,nc)] = t_next
                        heapq.heappush(h, (t_next, nr, nc, flag^1))