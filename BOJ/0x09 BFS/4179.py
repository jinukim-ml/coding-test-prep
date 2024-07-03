import sys
from collections import deque

input = sys.stdin.readline
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
board = []
fires = deque()

def bfs_fire(fires: deque, R, C, board, f_dist):
    while fires:
        X, Y = fires.popleft()
        for direction in range(4):
            nx = X + dx[direction]
            ny = Y + dy[direction]

            if nx < 0 or nx >= R or ny < 0 or ny >= C: continue
            if board[nx][ny] == '#' or f_dist[nx][ny] >= 0: continue

            fires.append([nx, ny])
            f_dist[nx][ny] = f_dist[X][Y] + 1
    return f_dist

def bfs(start_X, start_Y, R, C, board, f_dist):
    q = deque()
    q.append([start_X, start_Y])
    dist = [[-1] * C for _ in range(R)]
    dist[start_X][start_Y] += 1

    while len(q) > 0:
        X, Y = q.popleft()
        for direction in range(4):
            nx = X + dx[direction]
            ny = Y + dy[direction]

            if nx < 0 or nx >= R or ny < 0 or ny >= C: continue
            if board[nx][ny] != '.' or dist[nx][ny] >= 0: continue
            if f_dist[nx][ny] != -1 and f_dist[nx][ny] <= dist[X][Y]+1: continue

            q.append([nx, ny])
            dist[nx][ny] = dist[X][Y] + 1
    return dist

R, C = map(int, input().split())

jihoon_X, jihoon_Y = -1, -1
f_dist = [[-1] * C for _ in range(R)]

for i in range(R):
    board.append(list(input().rstrip()))
    for j in range(C):
        if board[i][j] == 'J': jihoon_X, jihoon_Y = i, j
        if board[i][j] == 'F':
            fires.append([i,j])
            f_dist[i][j] += 1

f_dist = bfs_fire(fires, R, C, board, f_dist)
j_dist = bfs(jihoon_X, jihoon_Y, R, C, board, f_dist)

min_dist = 10000000

for row in [0, R-1]:
    for col in range(C):
        if j_dist[row][col] <= min_dist and j_dist[row][col] != -1:
            min_dist = j_dist[row][col]

for col in [0, C-1]:
    for row in range(1, R):
        if j_dist[row][col] <= min_dist and j_dist[row][col] != -1:
            min_dist = j_dist[row][col]

if R == 1 and C == 1:
    print(1)
else:
    if min_dist == 10000000: print('IMPOSSIBLE')
    else: print(min_dist + 1)