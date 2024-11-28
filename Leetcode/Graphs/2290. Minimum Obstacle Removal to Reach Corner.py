from collections import deque

class Solution:
    def minimumObstacles(self, grid: list[list[int]]) -> int:
        # 0-1 BFS
        m, n = len(grid), len(grid[0])
        directions = [(-1,0), (0,1), (1,0), (0,-1)]
        distances = [[float('inf') for _ in range(n)] for _ in range(m)]
        distances[0][0] = 0
        q = deque([(0,0,0)])

        while q:
            r, c, dist = q.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if 0 <= nr < m and 0 <= nc < n and dist < distances[nr][nc]:
                    distances[nr][nc] = dist

                    if grid[nr][nc] == 1:
                        q.append((nr, nc, dist+1))
                    else:
                        q.appendleft((nr, nc, dist))
        return distances[m-1][n-1]