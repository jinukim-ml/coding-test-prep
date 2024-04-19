'''
Solution for https://school.programmers.co.kr/learn/courses/30/lessons/154538
Type: BFS
'''
from collections import deque
def solution(x, y, n):
    q = deque([x])
    cnt = 0
    visited = {x:1}
    while q:
        for _ in range(len(q)):
            val = q.popleft()
            if val == y:
                return cnt
            nx = val + n
            ny = 2*val
            nz = 3*val
            if nx <= y and nx not in visited:
                q.append(nx)
                visited[nx] = visited.get(nx, 0) + 1
            if ny <= y and ny not in visited:
                q.append(ny)
                visited[ny] = visited.get(ny, 0) + 1
            if nz <= y and nz not in visited:
                q.append(nz)
                visited[nz] = visited.get(nz, 0) + 1
        cnt += 1

    return -1