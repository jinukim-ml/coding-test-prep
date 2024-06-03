from typing import List
import heapq

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        directions = [(0,1), (1,0), (0,-1), (-1,0)]
        vis = set()
        vis.add((0,0))
        h = [(grid[0][0], 0, 0)]

        ans = grid[0][0]
        while h:
            height, r, c = heapq.heappop(h)
            ans = max(ans, height)
            if r == len(grid)-1 and c == len(grid[0])-1:
                return ans
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and (nr,nc) not in vis:
                    heapq.heappush(h, (grid[nr][nc], nr, nc))
                    vis.add((nr,nc))