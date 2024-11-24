class Solution:
    def maxMatrixSum(self, matrix: list[list[int]]) -> int:
        n = len(matrix)
        abs_total = 0
        min_abs = float('inf')
        negatives = 0
        for r in range(n):
            for c in range(n):
                if matrix[r][c] < 0:
                    negatives += 1
                absolute_val = abs(matrix[r][c])
                abs_total += absolute_val
                min_abs = min(min_abs, absolute_val)

        if negatives%2:
            return abs_total - 2 * min_abs
        else:
            return abs_total