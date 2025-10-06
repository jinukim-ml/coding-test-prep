import heapq

class Solution:
    def swimInWater(self, grid: list[list[int]]) -> int:
        n = len(grid)
        h = [(grid[0][0], 0, 0)]
        directions = [(-1,0), (0,1), (1,0), (0,-1)]
        visited = set()
        while h:
            t, r, c = heapq.heappop(h)
            if (r,c) in visited:
                continue
            visited.add((r,c))
            if r == n-1 and c == n-1:
                return t
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and (nr,nc) not in visited:
                    new_t = max(t, grid[nr][nc])
                    heapq.heappush(h, (new_t, nr, nc))