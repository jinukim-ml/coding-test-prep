class Solution: # O(1) using difference sequence
    def coloredCells(self, n: int) -> int:
        return 1 + 2 * n**2 - 2 * n