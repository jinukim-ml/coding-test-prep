from typing import List

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        self.heights = heights
        ans = []
        for r in range(len(heights)):
            for c in range(len(heights[0])):
                self.vis = {(r,c)}
                self.pac, self.atl = False, False
                self.dfs((r,c))
                if self.pac and self.atl:
                    ans.append([r,c])

        return ans
    def dfs(self, coords: tuple):
        r, c = coords
        if r == 0 or c == 0:
            self.pac = True
        if r == len(self.heights) - 1 or c == len(self.heights[0]) - 1:
            self.atl = True

        for d in [(0,1), (1,0), (0,-1), (-1,0)]:
            dr, dc = r + d[0], c + d[1]
            if (dr,dc) not in self.vis and 0 <= dr < len(self.heights) and 0 <= dc < len(self.heights[0]) and self.heights[r][c] >= self.heights[dr][dc]:
                self.vis.add((dr,dc))
                self.dfs((dr,dc))
            if self.pac and self.atl:
                return