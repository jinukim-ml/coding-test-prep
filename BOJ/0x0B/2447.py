import sys
input = sys.stdin.readline
write = sys.stdout.write

n = int(input())
board = [['*']*n for _ in range(n)]

def blank(x:int, y: int, length:int):
    for i in range(x, x+length):
            for j in range(y, y+length):
                board[i][j] = ' '

def star(x: int, y: int, n: int):
    if n == 3:
        board[x+1][y+1] = ' '
        return
    else:
        for i in range(3):
            for j in range(3):
                if i == j == 1:
                    blank(x+i*n//3, y+j*n//3, n//3)
                else:
                    star(x+i*n//3, y+j*n//3, n//3)

star(0, 0, n)
for i in range(n):
    for j in range(n):
        write(board[i][j])
    write('\n')