import sys
from collections import deque

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
q = deque()

M, N = map(int, sys.stdin.readline().split())
board = []
dist = [[0] * M for _ in range(N)]
farthest = 0
cnt = 0

for i in range(N):
    board.append(map(int, sys.stdin.readline().split()))
    for j, num in enumerate(board[i]):
        if num == 0:
            dist[i][j] = -1
            cnt += 1
        elif num == 1:
            q.append([i,j])

while q:
    X, Y = q.popleft()

    for dir in range(4):
        nx = X + dx[dir]
        ny = Y + dy[dir]

        if nx < 0 or nx >= N or ny < 0 or ny >= M: continue
        if dist[nx][ny] >= 0: continue
        q.append([nx, ny])
        dist[nx][ny] = dist[X][Y] + 1
        cnt -= 1
        if dist[nx][ny] > farthest:
            farthest = dist[nx][ny]

if cnt == 0: print(farthest)
else: print(-1)