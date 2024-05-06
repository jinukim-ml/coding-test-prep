from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.board = board
        self.word = word
        self.vis = {}

        starting_points = []
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0] and (i,j) not in self.vis:
                    starting_points.append((i,j))

        for coord in starting_points:
            y, x = coord
            self.vis[(y,x)] = True
            if self.DFS(coord, 1):
                return True
            self.vis.pop((y,x))
        return False

    def DFS(self, coord: tuple, length: int):
        if length == len(self.word):
            return True
        elif length < len(self.word):
            y, x = coord
            for d in [(0,1), (-1,0), (0,-1), (1,0)]:
                dy = y + d[0]
                dx = x + d[1]

                if 0 <= dx <= len(self.board[0])-1 and 0 <= dy <= len(self.board)-1 and self.board[dy][dx] == self.word[length] and (dy,dx) not in self.vis:
                    self.vis[(dy,dx)] = True
                    if self.DFS((dy,dx), length+1):
                        return True
                    self.vis.pop((dy,dx))

        return False