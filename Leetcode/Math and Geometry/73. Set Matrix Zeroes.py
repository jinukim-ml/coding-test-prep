from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        changed = {}
        i = 0
        while i < len(matrix):
            j = 0
            
            while j < len(matrix[0]):
                
                if matrix[i][j] == 0 and (i,j) not in changed:
                    col = 0
                    while col < len(matrix[0]): # change row
                        if matrix[i][col] == 0:
                            col += 1
                            continue
                        matrix[i][col] = 0
                        changed[(i,col)] = True
                        col += 1
                    
                    row = 0
                    while row < len(matrix): # change column
                        if matrix[row][j] == 0:
                            row += 1
                            continue
                        matrix[row][j] = 0
                        changed[(row,j)] = True
                        row += 1
                    
                j += 1
            i += 1

class Solution: # faster solution
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        
        zero_col = set()
        zero_row = set()
        
        for r in range(m):
            for c in range(n):
                if matrix[r][c] == 0:
                    zero_col.add(c)
                    zero_row.add(r)
                
        for r in zero_row:
            for c in range(n):
                matrix[r][c] = 0
        
        for r in range(m):
            for c in zero_col:
                matrix[r][c] = 0