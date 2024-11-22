class Solution:
    def maxEqualRowsAfterFlips(self, matrix: list[list[int]]) -> int:
        freq = {}
        for row in matrix:
            pattern = ''.join('T' if entry == row[0] else 'F' for entry in row)
            freq[pattern] = freq.get(pattern, 0) + 1
        return max(freq.values(), default=0)