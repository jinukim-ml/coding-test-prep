import sys

readline = sys.stdin.readline

n = int(readline())
board = [list(map(int, readline().split())) for _ in range(n)]
cnt = [0, 0, 0]

def check(x, y, n):
    for i in range(x, x+n):
        for j in range(y, y+n):
            if board[x][y] != board[i][j]:
                return False
    return True

def solve(x, y, z):
    if check(x, y, z):
        cnt[board[x][y] + 1] += 1
        return
    
    for i in range(3):
        for j in range(3):
            solve(x+i*z//3, y+j*z//3, z//3)

solve(0, 0, n)
print(cnt[0], cnt[1], cnt[2], sep='\n')