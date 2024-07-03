import sys

H, W = map(int, sys.stdin.readline().split())

mat = [list(map(int, input().split())) for _ in range(H)]

visited = [[0] * W for _ in range(H)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

num = 0
max_area = 0

for i in range(H):
    for j in range(W):
        if mat[i][j] == 0 or visited[i][j] == 1:
            # print('i,j:', i, j, 'CONTINUE')
            continue
        num +=1
        queue = []
        visited[i][j] = 1
        queue.append([i,j])
        area = 0

        while(len(queue) != 0):
            area += 1
            X, Y = queue.pop(0)

            # START OF BFS
            for dir in range(len(dx)):
                nx = X + dx[dir]
                ny = Y + dy[dir]

                if nx < 0 or nx >= H or ny < 0 or ny >= W: continue
                if visited[nx][ny] == 1 or mat[nx][ny] == 0: continue

                visited[nx][ny] = 1
                queue.append([nx, ny])
                # END OF BFS
            max_area = max(max_area, area)

print(num, max_area, sep='\n')