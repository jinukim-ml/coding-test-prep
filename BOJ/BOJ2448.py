import sys
input = sys.stdin.readline
write = sys.stdout.write

n = int(input())
board = [[' ']*(n*2-1) for _ in range(n)]

def star(x: int, y: int, n: int):
    if n == 3:
        board[x][y] = '*'
        board[x+1][y-1] = '*'
        board[x+1][y+1] = '*'
        for col in range(y-2, y+3):
            board[x+2][col] = '*'
        return
    else:
        star(x, y, n//2)
        star(x+n//2, y-(n-1)//2-1, n//2)
        star(x+n//2, y+(n//2), n//2)

star(0, n-1, n)
for i in range(n):
    for j in range(n*2-1):
        write(board[i][j])
    write('\n')