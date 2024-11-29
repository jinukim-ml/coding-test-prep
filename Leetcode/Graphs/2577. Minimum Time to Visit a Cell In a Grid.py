import heapq

class Solution:
    def minimumTime(self, grid: list[list[int]]) -> int:
        if grid[0][1] > 1 and grid[1][0] > 1:
            return - 1
        m, n = len(grid), len(grid[0])
        directions = [(-1,0), (0,1), (1,0), (0,-1)]
        distances = [[float('inf') for _ in range(n)] for _ in range(m)]
        distances[0][0] = 0
        
        h = []
        heapq.heappush(h, (0,0,0))
        while h:
            t, r, c = heapq.heappop(h)
            print(r, c)
            if r == m-1 and c == n-1:
                return t
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n:
                    if t >= grid[nr][nc]:
                        new_t = t+1
                    else:
                        if (grid[nr][nc] - t)%2: # odd
                            new_t = grid[nr][nc]
                        else: # even
                            new_t = grid[nr][nc]+1
                    
                    if new_t < distances[nr][nc]:
                        distances[nr][nc] = new_t
                        heapq.heappush(h, (new_t, nr, nc))