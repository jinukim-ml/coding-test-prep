class Solution:
    def luckyNumbers(self, matrix: list[list[int]]) -> list[int]:
        ans = []
        
        for r in range(len(matrix)):
            c = matrix[r].index(min(matrix[r]))
            cnt = 0
            for row in range(len(matrix)):
                if matrix[row][c] > matrix[r][c]:
                    break
                else:
                    cnt += 1
            if cnt == len(matrix):
                ans.append(matrix[r][c])
        
        return ans