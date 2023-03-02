import sys
from collections import deque

input = sys.stdin.readline
dist = [-1] * 100001
dx = [-1, 1, 2]

q = deque()

n, k = map(int, input().split())
q.append(n)
dist[n] += 1

while q:
    x = q.popleft()

    for direction in range(3):
        if direction < 2: nx = x + dx[direction]
        else: nx = 2*x

        if nx < 0 or nx > 100000: continue
        if dist[nx] >= 0: continue

        q.append(nx)
        dist[nx] = dist[x] + 1
        if nx == k: break
    if nx == k: break
print(dist[k])