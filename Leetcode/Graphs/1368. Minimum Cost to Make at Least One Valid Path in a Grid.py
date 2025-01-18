import heapq

class Solution:
    def minCost(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        target = (m-1, n-1)
        h = []
        heapq.heappush(h, (0, 0, 0))
        vis = set()
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        while h:
            cost, r, c = heapq.heappop(h)
            if (r, c) in vis:
                continue
            vis.add((r, c))
            if (r, c) == target:
                return cost
            
            for i, (dr, dc) in enumerate(directions):
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and (nr, nc) not in vis:
                    if grid[r][c] == i+1:
                        heapq.heappush(h, (cost, nr, nc))
                    else:
                        heapq.heappush(h, (cost+1, nr, nc))