class Solution: # classic DFS solution. O(n^2)
    def islandPerimeter(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        visited = set()
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        def dfs(r: int, c: int, val: int) -> int:
            visited.add((r,c))
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if not 0 <= nr < m or not 0 <= nc < n or grid[nr][nc] == 0: # is the next point water?
                    val += 1
                elif (nr,nc) not in visited: # continued land
                    val += dfs(nr, nc, 0)
            return val
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c]:
                    return dfs(r, c, 0)

class Solution: # Same O(n^2) but faster
    def islandPerimeter(self, grid: list[list[int]]) -> int:
        ans = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c]:
                    ans += 4
                    if r > 0 and grid[r-1][c]:
                        ans -= 2
                    if c > 0 and grid[r][c-1]:
                        ans -= 2
        return ans