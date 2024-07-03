import sys

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def initialize(M, N):
    mat = [[0] * M for _ in range(N)]
    vis = [[0] * M for _ in range(N)]
    return mat, vis

def BFS(M, N, mat, vis):
    bugs = 0
    q = []
    for i in range(N):
        for j in range(M):
            if mat[i][j] == 0 or vis[i][j] != 0: continue
            q.append([i,j])
            vis[i][j] += 1
            bugs += 1
            while(len(q) != 0):
                Y, X = q.pop(0)
                for dir in range(4):
                    nx = X + dx[dir]
                    ny = Y + dy[dir]

                    if nx < 0 or nx >= M or ny < 0 or ny >= N: continue
                    if mat[ny][nx] == 0 or vis[ny][nx] != 0: continue
                    
                    q.append([ny, nx])
                    vis[ny][nx] += 1
    print(bugs)

num_cases = int(sys.stdin.readline().rstrip())
for _ in range(num_cases):
    M, N, K = map(int, sys.stdin.readline().strip().split())
    mat, vis = initialize(M, N)
    for _ in range(K):
        X, Y = map(int, sys.stdin.readline().strip().split())
        mat[Y][X] += 1
    BFS(M, N, mat, vis)