from typing import List
from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        directions = [(0,1), (1,0), (0,-1), (-1,0)]
        def bfs(oy: int, ox: int) -> None:
            vis = set()
            q = deque([(oy,ox)])
            distance = 0
            
            while q:
                for _ in range(len(q)):
                    r, c = q.popleft()
                    grid[r][c] = min(grid[r][c], distance)
                    for dr, dc in directions:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and (nr,nc) not in vis and grid[nr][nc] > 0:
                            vis.add((nr,nc))
                            q.append((nr,nc))
                distance += 1
        
        chests = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    chests.append((i,j))

        for y, x in chests:
            bfs(y, x)