from collections import deque

class Solution:
    def highestPeak(self, isWater: list[list[int]]) -> list[list[int]]:
        m, n = len(isWater), len(isWater[0])
        dq = deque()
        vis = set()
        for r in range(m):
            for c in range(n):
                if isWater[r][c]:
                    dq.append((r,c))
                    vis.add((r, c))
        
        res = [[0 for _ in range(n)] for _ in range(m)]
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        dist = 0
        while dq:
            for _ in range(len(dq)):
                r, c = dq.popleft()
                res[r][c] = dist
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < m and 0 <= nc < n and (nr, nc) not in vis:
                        dq.append((nr, nc))
                        vis.add((nr, nc))
            dist += 1
        return res