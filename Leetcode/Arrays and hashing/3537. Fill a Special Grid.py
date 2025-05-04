class Solution:
    def specialGrid(self, n: int) -> list[list[int]]:
        if n == 0:
            return [[0]]
        length = 2**n
        res = [[0 for _ in range(length)] for _ in range(length)]
        val = 0
        def fill_grid(r_start: int, r_end: int, c_start: int, c_end: int) -> None:
            nonlocal val
            if r_end - r_start == 1:
                res[r_start][c_end] = val
                res[r_end][c_end] = val + 1
                res[r_end][c_start] = val + 2
                res[r_start][c_start] = val + 3
                val += 4
                return
            row_half = (r_start + r_end) // 2
            col_half = (c_start + c_end) // 2
            fill_grid(r_start, row_half, col_half+1, c_end) # upper right
            fill_grid(row_half+1, r_end, col_half+1, c_end) # bottom right
            fill_grid(row_half+1, r_end, c_start, col_half) # bottom left
            fill_grid(r_start, row_half, c_start, col_half) # upper left

        fill_grid(0, length-1, 0, length-1)
        return res