class Solution:
    def minOperations(self, grid: list[list[int]], x: int) -> int:
        arr = []
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                arr.append(grid[r][c])
        del grid
        arr.sort()
        target = arr[len(arr)//2]
        res = 0
        for n in arr:
            if n % x != target % x:
                return -1
            res += abs(n - target) // x
        return res