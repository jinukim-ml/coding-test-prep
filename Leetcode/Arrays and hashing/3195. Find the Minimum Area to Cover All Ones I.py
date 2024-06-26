from typing import List

class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        up, left = float('inf'), float('inf')
        down, right = -1, -1
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    up = min(up, r)
                    left = min(left, c)
                    right = max(right, c)
                    down = max(down, r)
        return (down-up+1)*(right-left+1)