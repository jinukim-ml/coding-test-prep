from typing import List
from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        directions = [(0,1), (1,0), (0,-1), (-1,0)]
        q = deque()
        fresh = set()
        vis = set()
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    fresh.add((r,c))
                if grid[r][c] == 2:
                    q.append((r,c))
                    vis.add((r,c))

        if len(fresh) == 0:
            return 0

        t = -1
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    
                    if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] == 1 and (nr,nc) not in vis:
                        q.append((nr,nc))
                        vis.add((nr,nc))
                        grid[nr][nc] = 2
            t += 1
        
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    return -1
        return t