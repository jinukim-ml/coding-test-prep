import sys

H, W = map(int, sys.stdin.readline().split())
mat = [list(map(int, sys.stdin.readline().strip())) for _ in range(H)]
dist = [[-1] * W for _ in range(H)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

q = []
dist[0][0] = 0
q.append([0,0])

while(len(q) != 0):
    X, Y = q.pop(0)
    
    for dir in range(4):
        nx = X + dx[dir]
        ny = Y + dy[dir]

        if nx < 0 or nx >= H or ny < 0 or ny >= W: continue
        if dist[nx][ny] >= 0 or mat[nx][ny] == 0: continue

        dist[nx][ny] = dist[X][Y] + 1
        q.append([nx, ny])
print(dist[H-1][W-1]+1)