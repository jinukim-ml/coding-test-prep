from collections import deque

class Solution:
    def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
        m, n = len(image), len(image[0])
        directions = [(-1,0), (0,1), (1,0), (0,-1)]
        target = image[sr][sc]
        q = deque([(sr,sc)])
        visited = set()
        while q:
            r, c = q.popleft()
            image[r][c] = color
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and image[nr][nc] == target and (nr,nc) not in visited:
                    q.append((nr,nc))
                    visited.add((nr,nc))
        return image