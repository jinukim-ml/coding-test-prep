from typing import List
from collections import deque

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ans = 0
        directions = [(0,1), (1,0), (0,-1), (-1,0)]
        vis = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 and (i,j) not in vis:
                    vis.add((i,j))
                    q = deque([(i,j)])
                    area = 0
                    while q:
                        area += 1
                        r, c = q.popleft()
                        for dr, dc in directions:
                            nr, nc = r + dr, c + dc
                            if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and (nr,nc) not in vis and grid[nr][nc] == 1:
                                vis.add((nr,nc))
                                q.append((nr,nc))
                    ans = max(ans, area)
        
        return ans