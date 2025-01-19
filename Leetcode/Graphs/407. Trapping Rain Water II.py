import heapq

class Solution:
    def trapRainWater(self, heightMap: list[list[int]]) -> int:
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        m, n = len(heightMap), len(heightMap[0])
        if m <= 2 or n <= 2:
            return 0
        
        boundary = []
        for i in range(m):
            boundary.append((heightMap[i][0], i, 0))
            boundary.append((heightMap[i][-1], i, n-1))
            heightMap[i][0] = heightMap[i][-1] = -1
        
        for j in range(1, n-1):
            boundary.append((heightMap[0][j], 0, j))
            boundary.append((heightMap[-1][j], m-1, j))
            heightMap[0][j] = heightMap[-1][j] = -1

        heapq.heapify(boundary)
        res, water_level = 0, 0
        while boundary:
            h, r, c = heapq.heappop(boundary)
            water_level = max(water_level, h)
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and heightMap[nr][nc] != -1:
                    curr_height = heightMap[nr][nc]
                    if curr_height < water_level:
                        res += water_level - curr_height
                    heightMap[nr][nc] = -1
                    heapq.heappush(boundary, (curr_height, nr, nc))
        return res