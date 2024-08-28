class Solution:
    def countSubIslands(self, grid1: list[list[int]], grid2: list[list[int]]) -> int:
        m, n = len(grid1), len(grid1[0])
        directions = [(-1,0), (0,1), (1,0), (0,-1)]
        
        def dfs2(r:int, c:int, seen:set, coords:set) -> None:
            if not 0 <= r < m or not 0 <= c < n or grid2[r][c] == 0 or (r,c) in seen:
                return
            
            seen.add((r, c))
            coords.add((r,c))
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                dfs2(nr, nc, seen, coords)

        ans = 0
        seen = set()
        for r in range(m):
            for c in range(n):
                if grid2[r][c] == 1 and (r,c) not in seen:
                    coords = set()
                    dfs2(r, c, seen, coords)
                    cnt = 0
                    for x, y in coords:
                        if grid1[x][y] == 0: break
                        else: cnt += 1
                    if cnt == len(coords):
                        ans += 1
        return ans