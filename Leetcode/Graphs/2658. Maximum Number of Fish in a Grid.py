from collections import deque

class Solution:
    def findMaxFish(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        visited = set()
        def bfs(r: int, c: int) -> int:
            dq = deque()
            dq.append((r, c))
            visited.add((r, c))
            fish = 0
            while dq:
                r, c = dq.popleft()
                fish += grid[r][c]
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] and (nr, nc) not in visited:
                        dq.append((nr, nc))
                        visited.add((nr, nc))
            return fish
        
        res = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] and (r,c) not in visited:
                    res = max(res, bfs(r, c))
        return res