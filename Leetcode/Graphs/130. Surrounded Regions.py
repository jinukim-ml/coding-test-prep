from typing import List
from collections import deque

class Solution: # BFS solution
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        vis = set()
        directions = [(0,1), (1,0), (0,-1), (-1,0)]
        def bfs(coords: tuple):
            q = deque()
            q.append(coords)
            vis.add(coords)
            while q:
                r, c = q.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < len(board) and 0 <= nc < len(board[0]) and (nr,nc) not in vis and board[nr][nc] == 'O':
                        q.append((nr,nc))
                        vis.add((nr,nc))
                        board[nr][nc] = 'N'

        for r in [0, len(board)-1]:
            for c in range(len(board[0])):
                if board[r][c] == 'O' and (r,c) not in vis:
                    bfs((r,c))
        
        for r in range(len(board)):
            for c in [0, len(board[0])-1]:
                if board[r][c] == 'O' and (r,c) not in vis:
                    bfs((r,c))
        
        for r in range(1, len(board)-1):
            for c in range(1, len(board[0])-1):
                if board[r][c] == 'O':
                    board[r][c] = 'X'

        for r,c in vis:
            board[r][c] = 'O'

class Solution: # DFS solution
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])

        def capture(r, c):
            if r < 0 or c < 0 or r == ROWS or c == COLS or board[r][c] != "O":
                return
            board[r][c] = "T"
            capture(r + 1, c)
            capture(r - 1, c)
            capture(r, c + 1)
            capture(r, c - 1)

        # 1. (DFS) Capture unsurrounded regions (O -> T)
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O" and (r in [0, ROWS - 1] or c in [0, COLS - 1]):
                    capture(r, c)

        # 2. Capture surrounded regions (O -> X)
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"

        # 3. Uncapture unsurrounded regions (T -> O)
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "T":
                    board[r][c] = "O"