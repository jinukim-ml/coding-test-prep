class Solution: # time complexity: O(mn), space complexity: O(m+n)
    def setZeroes(self, matrix: list[list[int]]) -> None:
        m, n = len(matrix), len(matrix[0])
        h = set()
        v = set()
        for r in range(m):
            for c in range(n):
                if matrix[r][c] == 0:
                    h.add(r)
                    v.add(c)
        
        for r in h:
            matrix[r] = [0]*n
        for c in v:
            for r in range(m):
                matrix[r][c] = 0

class Solution: # time complexity: O(mn), space complexity: O(1)
    def setZeroes(self, matrix: list[list[int]]) -> None:
        m, n = len(matrix), len(matrix[0])
        r_flag, c_flag = False, False
        for c in range(n):
            if matrix[0][c] == 0:
                r_flag = True
                break
        
        for r in range(m):
            if matrix[r][0] == 0:
                c_flag = True
                break
        
        for r in range(1, m):
            for c in range(1, n):
                if matrix[r][c] == 0:
                    matrix[r][0] = 0
                    matrix[0][c] = 0
        
        for r in range(1, m):
            for c in range(1, n):
                if matrix[r][0] == 0 or matrix[0][c] == 0:
                    matrix[r][c] = 0

        if r_flag: # if true, set the first row to zeros
            matrix[0] = [0]*n
        if c_flag:
            for r in range(m):
                matrix[r][0] = 0