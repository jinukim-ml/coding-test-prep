import heapq

class Solution:
    def maxPoints(self, grid: list[list[int]], queries: list[int]) -> list[int]:
        m, n = len(grid), len(grid[0])
        res = [0] * len(queries)
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        sorted_queries = sorted([(val, i) for i, val in enumerate(queries)])

        h = [(grid[0][0], 0, 0)]
        visited = set([(0, 0)])
        points = 0
        for q, i in sorted_queries:
            while h and h[0][0] < q:
                _, r, c = heapq.heappop(h)
                points += 1
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < m and 0 <= nc < n and (nr, nc) not in visited:
                        heapq.heappush(h, (grid[nr][nc], nr, nc))
                        visited.add((nr, nc))
            res[i] = points
        return res