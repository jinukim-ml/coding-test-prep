from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # transpose
        for d in range(len(matrix)):
            for c in range(d+1, len(matrix)):
                matrix[d][c], matrix[c][d] = matrix[c][d], matrix[d][c]
        
        # reverse
        for r in range(len(matrix)):
            matrix[r] = reversed(matrix[r])