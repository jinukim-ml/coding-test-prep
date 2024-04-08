'''
Solution for https://school.programmers.co.kr/learn/courses/30/lessons/159993
Type: BFS
'''
from collections import deque
def solution(maps):
    distance, found = 0, False
    lever_x, lever_y = -1, -1
    m = len(maps)
    n = len(maps[0])

    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    vis = [[False] * n for _ in range(m)]

    q = deque()
    for i in range(m): # Find starting point
        for j in range(n):
            if maps[i][j] == 'S':
                q.append([i,j])
                vis[i][j] = True
                break
        if q:
            break

    while q:
        for _ in range(len(q)):
            Y, X = q.popleft()
            for direction in range(4):
                nx = X + dx[direction]
                ny = Y + dy[direction]
                if 0 <= nx < n and 0 <= ny < m and vis[ny][nx] == False and maps[ny][nx] != 'X':
                    if maps[ny][nx] == 'L':
                        lever_x, lever_y = nx, ny
                        found = True
                        break
                    else:
                        q.append([ny, nx])
                        vis[ny][nx] = True

        distance += 1
        if found == True:
            break
        
    # Reset queue, and visted
    if lever_x == -1 and lever_y == -1:
        return -1
    else:
        q = deque([[lever_y, lever_x]])
        vis = [[False] * n for _ in range(m)]
        vis[lever_y][lever_x] = True
    
        while q:
            for _ in range(len(q)):
                Y, X = q.popleft()
                
                for direction in range(4):
                    nx = X + dx[direction]
                    ny = Y + dy[direction]

                    if 0 <= nx < n and 0 <= ny < m and vis[ny][nx] == False and maps[ny][nx] != 'X':
                        if maps[ny][nx] == 'E':
                            return distance+1
                        else:
                            q.append([ny,nx])
                            vis[ny][nx] = True
            distance += 1
        return -1