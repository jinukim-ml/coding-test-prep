import sys
input = sys.stdin.readline
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
map = []

def paint_map(map, color: str):
    N = len(map[0])
    painted_map = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if map[i][j] == color:
                painted_map[i][j] = 1
    return painted_map

def BFS(N, map):
    q = []
    vis = [[0] * N for _ in range(N)]
    cnt = 0
    
    for i in range(N):
        for j in range(N):
            if map[i][j] == 0 or vis[i][j] > 0: continue
            q.append([i,j])
            vis[i][j] += 1
            cnt += 1
            while len(q) != 0:
                X, Y = q.pop(0)
                for dir in range(4):
                    nx = X + dx[dir]
                    ny = Y + dy[dir]

                    if nx < 0 or nx >= N or ny < 0 or ny >= N: continue
                    if map[nx][ny] == 0 or vis[nx][ny] > 0: continue
                    vis[nx][ny] += 1
                    q.append([nx, ny])
    return cnt

def BFS_RG(N, map):
    map_colorblinded = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if map[i][j] == 'G':
                map_colorblinded[i][j] = 'R'
            else:
                map_colorblinded[i][j] = map[i][j]
    map_colorblinded = paint_map(map_colorblinded, 'R')
    area = BFS(N, map_colorblinded)
    return area

N = int(sys.stdin.readline())
for _ in range(N):
    line = list(input().rstrip())
    map.append(line)

red = paint_map(map, 'R')
green = paint_map(map, 'G')
blue = paint_map(map, 'B')
blue_area = BFS(N, blue)
red_area = BFS(N, red)
green_area = BFS(N, green)
colorblinded = BFS_RG(N, map)

print('{} {}'.format(blue_area+red_area+green_area, blue_area+colorblinded))