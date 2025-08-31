from collections import defaultdict

class Solution:
    def solveSudoku(self, board: list[list[str]]) -> None:
        rows = defaultdict(set)
        cols = defaultdict(set)
        subgrids = defaultdict(set)
        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val != '.':
                    val = int(val)
                    rows[r].add(val)
                    cols[c].add(val)
                    subgrids[r//3*3+c//3].add(val)
        
        def is_valid(r: int, c: int, val: int) -> bool:
            if val in rows[r] or val in cols[c] or val in subgrids[r//3*3+c//3]:
                return False
            return True

        def place_num(r: int, c: int, val: int) -> None:
            rows[r].add(val)
            cols[c].add(val)
            subgrids[r//3*3+c//3].add(val)
            board[r][c] = str(val)
        
        def delete_num(r: int, c: int, val: int) -> None:
            rows[r].discard(val)
            cols[c].discard(val)
            subgrids[r//3*3+c//3].discard(val)
            board[r][c] = '.'

        def backtrack(r: int, c: int) -> bool:
            if board[r][c] != '.': # non-empty cell
                if r == 8 and c == 8:
                    return True
                elif c == 8:
                    return backtrack(r+1, 0)
                else:
                    return backtrack(r, c+1)
            else: # empty cell
                if r == 8 and c == 8:
                    for val in range(1, 10):
                        if is_valid(r, c, val):
                            board[r][c] = str(val)
                            return True
                elif c == 8:
                    for val in range(1, 10):
                        if is_valid(r, c, val):
                            place_num(r, c, val)
                            if backtrack(r+1, 0):
                                return True
                            delete_num(r, c, val)
                else:
                    for val in range(1, 10):
                        if is_valid(r, c, val):
                            place_num(r, c, val)
                            if backtrack(r, c+1):
                                return True
                            delete_num(r, c, val)
            return False
        backtrack(0, 0)