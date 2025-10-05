from collections import deque

class Solution:
    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
        m, n = len(heights), len(heights[0])
        directions = [(-1,0), (0,1), (1,0), (0,-1)]
        
        pacific, atlantic = deque(), deque()
        for r in range(m):
            pacific.append((r,0))
            atlantic.append((r, n-1))
        for c in range(1, n):
            pacific.append((0,c))
            atlantic.append((m-1, c))
        atlantic.pop() # remove the duplicate (m-1,n-1)
        atlantic.append((m-1,0))
        
        visited_pacific = set()
        while pacific:
            r, c = pacific.popleft()
            visited_pacific.add((r,c))
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and (nr,nc) not in visited_pacific and heights[nr][nc] >= heights[r][c]:
                    pacific.append((nr,nc))
        
        visited_atlantic = set()
        while atlantic:
            r, c = atlantic.popleft()
            visited_atlantic.add((r,c))
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and (nr,nc) not in visited_atlantic and heights[nr][nc] >= heights[r][c]:
                    atlantic.append((nr,nc))
        
        res = []
        for r, c in visited_pacific:
            if (r,c) in visited_atlantic:
                res.append([r,c])
        return res