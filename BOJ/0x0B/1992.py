import sys
readline = sys.stdin.readline

n = int(readline())
board = [list(map(int, list(readline().rstrip()))) for _ in range(n)]
ans = []

def check(x, y, length):
    for i in range(x, x+length):
        for j in range(y, y+length):
            if board[x][y] != board[i][j]: return False
    return True

def solve(x, y, length):
    if check(x, y, length):
        ans.append(board[x][y])
    else:
        ans.append('(')
        for i in range(2):
            for j in range(2):
                solve(x+i*length//2, y+j*length//2, length//2)
        ans.append(')')

solve(0, 0, n)
for i in range(len(ans)):
    print(ans[i], end='')