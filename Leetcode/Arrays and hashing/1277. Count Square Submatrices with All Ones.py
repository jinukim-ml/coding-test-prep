class Solution: # DP solution
    def countSquares(self, matrix: list[list[int]]) -> int:
        row, col = len(matrix), len(matrix[0])
        dp = [[0] * (col + 1) for _ in range(row + 1)]
        ans = 0
        for i in range(row):
            for j in range(col):
                if matrix[i][j]:
                    dp[i + 1][j + 1] = (min(dp[i][j + 1], dp[i + 1][j], dp[i][j]) + 1)
                    ans += dp[i + 1][j + 1]
        return ans

class Solution: # brute force solution
    def countSquares(self, matrix: list[list[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        ans = 0
        for sq_size in range(1, min(m, n)+1):
            row_start = 0
            local_ans = 0
            while row_start <= m - sq_size + 1:
                col_start = 0
                while col_start <= n - sq_size + 1:
                    cnt = 0
                    for r in range(row_start, row_start + sq_size):
                        for c in range(col_start, col_start + sq_size):
                            if r < m and c < n and matrix[r][c] == 1:
                                cnt += 1
                            else:
                                break
                        else:
                            continue
                        break
                    
                    if cnt == sq_size ** 2:
                        local_ans += 1
                    col_start += 1
                
                row_start += 1
            ans += local_ans
            
        return ans