from collections import Counter
from typing import List
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(len(board)): # check rows
            counter = Counter(board[i])
            counter.pop('.')
            if counter and counter.most_common(1)[0][1] >= 2:
                return False
        
        transpose = list(zip(*board))
        for col in transpose: # check columns
            counter = Counter(col)
            counter.pop('.')
            if counter and counter.most_common(1)[0][1] >= 2:
                return False
        
        for i in range(0, 9, 3): # 3x3 grid check
            for j in range(0, 9, 3):
                grid = []
                for row in range(i, i+3):
                    grid += (board[row][j:j+3])
                counter = Counter([*grid])
                counter.pop('.')
                if counter and counter.most_common(1)[0][1] >= 2:
                    return False
        
        return True