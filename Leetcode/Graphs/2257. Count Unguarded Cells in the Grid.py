from collections import deque

class Solution:
    def countUnguarded(self, m: int, n: int, guards: list[list[int]], walls: list[list[int]]) -> int:
        grid = [[0 for _ in range(n)] for _ in range(m)]
        for r, c in walls:
            grid[r][c] = 1
        
        directions = [(-1,0), (0,1), (1,0), (0,-1)]
        
        q = deque()
        for r, c in guards:
            for d in range(4):
                q.append((r,c,d))
            grid[r][c] = 1
        
        visited = set()
        while q:
            r, c, d = q.popleft()
            visited.add((r,c))
            dr, dc = directions[d]
            nr, nc = r + dr, c + dc
            if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == 0:
                q.append((nr,nc,d))
        
        return m*n - len(visited) - len(walls)