from typing import List

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        dp = {}
        directions = [(0,1), (1,0), (0,-1), (-1,0)]
        def dfs(r, c):
            if (r,c) in dp:
                return dp[(r,c)]
            
            longest = 1
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < len(matrix) and 0 <= nc < len(matrix[0]) and matrix[r][c] < matrix[nr][nc]:
                    longest = max(longest, 1 + dfs(nr, nc))
            dp[(r,c)] = longest
            return dp[(r,c)]
        
        ans = 0
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                ans = max(ans, dfs(r, c))
        return ans