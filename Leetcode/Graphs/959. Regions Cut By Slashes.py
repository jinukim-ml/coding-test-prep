class Solution:
    def regionsBySlashes(self, grid: list[str]) -> int:
        n = len(grid)
        L = 3 * n
        graph = [[0 for __ in range(L)] for _ in range(L)]
        directions = [(-1,0), (0,1), (1,0), (0,-1)]
        for i in range(n):
            for j in range(n):
                if grid[i][j] == '/':
                    for d in range(3): # fill the diagonal entries in 3x3
                        graph[3*i + 2 - d][3*j + d] = 1
                elif grid[i][j] == '\\':
                    for d in range(3): # fill the diagonal entries in 3x3
                        graph[3*i + d][3*j + d] = 1
        
        def dfs(r: int, c: int) -> None:
            if r < 0 or r >= L or c < 0 or c >= L or graph[r][c] == 1:
                return
            graph[r][c] = 1
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                dfs(nr, nc)
        
        ans = 0
        for r in range(L):
            for c in range(L):
                if graph[r][c] == 0:
                    dfs(r, c)
                    ans += 1
        return ans