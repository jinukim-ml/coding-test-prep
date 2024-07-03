import sys

readline = sys.stdin.readline

n = int(readline())
board = [list(map(int, readline().split())) for _ in range(n)]
cnt = [0, 0]

def check(x, y, length):
    for i in range(x, x+length):
        for j in range(y, y+length):
            if board[x][y] != board[i][j]: return False
    return True

def solve(x, y, length):
    if check(x, y, length):
        cnt[board[x][y]] += 1
        return
    else:   
        for i in range(2):
            for j in range(2):
                solve(x+i*length//2, y+j*length//2, length//2)

solve(0, 0, n)
print(cnt[0], cnt[1], sep='\n')