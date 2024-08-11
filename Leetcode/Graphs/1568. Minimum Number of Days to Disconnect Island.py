class Solution:
    def minDays(self, grid: list[list[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [(-1,0), (0,1), (1,0), (0,-1)]

        seen = set()
        candidates = set()
        def dfs(r: int, c: int) -> None:
            if not 0 <= r < rows or not 0 <= c < cols or grid[r][c] == 0 or (r,c) in seen:
                return
            
            seen.add((r,c))
            # candidate check
            if c > 0 and r + 1 < rows and grid[r][c-1] and grid[r+1][c]:
                candidates.add((r,c))
            elif r > 0 and c + 1 < cols and grid[r-1][c] and grid[r][c+1]:
                candidates.add((r,c))
            elif r + 1 < rows and c + 1 < cols and grid[r+1][c] and grid[r][c+1]:
                candidates.add((r,c))
            elif r > 0 and c > 0 and grid[r][c-1] and grid[r-1][c]:
                candidates.add((r,c))
            elif 0 < c < cols-1 and grid[r][c-1] and grid[r][c+1]:
                candidates.add((r,c))
            elif 0 < r < rows-1 and grid[r-1][c] and grid[r+1][c]:
                candidates.add((r,c))

            for dr, dc in directions:
                dfs(r + dr, c + dc)

        islands = 0
        ones = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    ones += 1
                    if (r,c) not in seen:
                        dfs(r,c)
                        islands += 1
        
        if islands == 0 or islands > 1:
            return 0
        elif ones == 1:
            return 1
        
        for candidate_r, candidate_c in candidates:
            seen = set()
            islands = 0
            grid[candidate_r][candidate_c] = 0
            for dr, dc in directions:
                nr, nc = candidate_r + dr, candidate_c + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] and (nr,nc) not in seen:
                    dfs(nr, nc)
                    islands += 1
                    if islands >= 2:
                        break
            else:
                grid[candidate_r][candidate_c] = 1
                continue
            break
        
        if islands >= 2:
            return 1
        else:
            return 2