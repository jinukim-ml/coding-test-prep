import sys
input = sys.stdin.readline

def star(n: int, x: int, y:int):
    if n == 1:
        board[x][y] = '*'
        return
    for i in range(3):
        for j in range(3):
            if i == j == 1:
                continue
            star(n//3, x + n//3 * i, y + n//3 * j)
            
n = int(input())
board = [[' ']*n for _ in range(n)]
star(n, 0, 0)

for i in range(n):
    for j in range(n):
        sys.stdout.write(board[i][j])
    sys.stdout.write('\n')