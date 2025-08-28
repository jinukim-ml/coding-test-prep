class Solution:
    def sortMatrix(self, grid: list[list[int]]) -> list[list[int]]:
        n = len(grid)
        # bottom-left
        for r0 in range(n):
            r1, c1 = r0, 0
            arr = []
            while r1 < n:
                arr.append(grid[r1][c1])
                r1 += 1
                c1 += 1
            arr.sort(reverse=True)
            r1, c1 = r0, 0
            while r1 < n:
                grid[r1][c1] = arr[r1-r0]
                r1 += 1
                c1 += 1
        # top-right
        for c0 in range(1, n):
            r1, c1 = 0, c0
            arr = []
            while c1 < n:
                arr.append(grid[r1][c1])
                r1 += 1
                c1 += 1
            arr.sort()
            r1, c1 = 0, c0
            while c1 < n:
                grid[r1][c1] = arr[c1-c0]
                r1 += 1
                c1 += 1
        return grid