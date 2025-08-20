from collections import deque

class Solution:
    def maxDistance(self, grid: list[list[int]]) -> int:
        n = len(grid)
        dist = [[float('inf') for _ in range(n)] for _ in range(n)]
        q = deque()
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    q.append((r,c))
                    dist[r][c] = 0
        if not q or len(q) == n*n:
            return -1
        
        res = 0
        directions = [(-1,0), (0,1), (1,0), (0,-1)]
        while q:
            r, c = q.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 0 and dist[nr][nc] > dist[r][c]+1:
                    q.append((nr, nc))
                    dist[nr][nc] = dist[r][c] + 1
                    res = max(res, dist[nr][nc])
        return res