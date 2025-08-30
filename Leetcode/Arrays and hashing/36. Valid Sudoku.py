from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        subgrids = defaultdict(set)
        for r in range(9):
            for c in range(9):
                if board[r][c] != '.':
                    section_num = r//3*3+c//3
                    if board[r][c] != '.' and board[r][c] in rows[r] or board[r][c] in cols[c] or board[r][c] in subgrids[section_num]:
                        return False
                    rows[r].add(board[r][c])
                    cols[c].add(board[r][c])
                    subgrids[section_num].add(board[r][c])
        return True