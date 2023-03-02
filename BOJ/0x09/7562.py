import sys

dx = [2, 1, -1, -2, -2, -1, 1, 2]
dy = [1, 2, 2, 1, -1, -2, -2, -1]

def BFS(cur_X, cur_Y, tar_X, tar_Y, dist, L):
    q = [[cur_X, cur_Y]]
    dist[cur_X][cur_Y] = 0
    
    while len(q) != 0:
        X, Y = q.pop(0)
        for i in range(8):
            nx = X + dx[i]
            ny = Y + dy[i]

            if nx < 0 or nx >= L or ny < 0 or ny >= L: continue
            if dist[nx][ny] >= 0: continue
            dist[nx][ny] = dist[X][Y] + 1
            q.append([nx, ny])
    sys.stdout.write(str(dist[tar_X][tar_Y])+'\n')

T = int(sys.stdin.readline())
for _ in range(T):
    L = int(sys.stdin.readline())
    cur_X, cur_Y = map(int, sys.stdin.readline().split())
    tar_X, tar_Y = map(int, sys.stdin.readline().split())

    dist = [[-1] * (L+1) for _ in range(L+1)]
    BFS(cur_X, cur_Y, tar_X, tar_Y, dist, L)