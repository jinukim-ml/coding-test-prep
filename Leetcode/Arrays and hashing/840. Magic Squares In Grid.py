class Solution:
    def numMagicSquaresInside(self, grid: list[list[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        if rows < 3 or cols < 3:
            return 0
        
        left, right = 0, 2
        up, down = 0, 2
        ans, contiguous = 0, 0
        while down < rows:
            left, right = 0, 2
            while right < cols:
                s = set()
                for r in range(up, down+1): # row sum
                    s.add(grid[r][left] + grid[r][left+1] + grid[r][right])
                for c in range(left, right+1): # column sum
                    s.add(grid[up][c] + grid[up+1][c] + grid[down][c])
                s.add(grid[up][left] + grid[up+1][left+1] + grid[down][right])
                s.add(grid[down][left] + grid[up+1][left+1] + grid[up][right])
                
                if len(s) > 1: # not a magic square, skip
                    left += 1
                    right += 1
                    continue
                
                # 1 - 9?
                seen = set()
                for r in range(up, down+1):
                    for c in range(left, right+1):
                        if grid[r][c] in seen or grid[r][c] == 0 or grid[r][c] > 9:
                            break
                        else:
                            seen.add(grid[r][c])
                    else: # a magic square
                        continue
                    break # not a magic square
                left += 1
                right += 1
                
                if len(seen) == 9:
                    contiguous += 1
                ans = max(ans, contiguous)
            up += 1
            down += 1
        return ans