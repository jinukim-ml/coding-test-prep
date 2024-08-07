class neighborSum:

    def __init__(self, grid: list[list[int]]):
        self.grid = grid
        self.m, self.n = len(grid), len(grid[0])
        self.book = {}
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                self.book[grid[r][c]] = (r,c)

    def adjacentSum(self, value: int) -> int:
        res = 0
        r, c = self.book[value]
        dr = [-1, 0, 1, 0]
        dc = [0, 1, 0, -1]
        
        for direction in range(4):
            nr, nc = r + dr[direction], c + dc[direction]
            if 0 <= nr < self.m and 0 <= nc < self.n:
                res += self.grid[nr][nc]
        return res

    def diagonalSum(self, value: int) -> int:
        res = 0
        r, c = self.book[value]
        dr = [-1, -1, 1, 1]
        dc = [-1, 1, -1, 1]

        for direction in range(4):
            nr, nc = r + dr[direction], c + dc[direction]
            if 0 <= nr < self.m and 0 <= nc < self.n:
                res += self.grid[nr][nc]
        return res


# Your neighborSum object will be instantiated and called as such:
# obj = neighborSum(grid)
# param_1 = obj.adjacentSum(value)
# param_2 = obj.diagonalSum(value)