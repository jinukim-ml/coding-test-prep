import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
indices = deque(map(int, input().split()))
q = deque(range(1, n+1))
ans = 0

while indices:
    if indices[0] == q[0]:
        from_q = q.popleft()
        popped = indices.popleft()
        continue

    left, right = 0, 0
    temp_q = deque()
    temp_q2 = deque()
    for i in range(len(q)):
        temp_q.append(q[i])
        temp_q2.append(q[i])

    while indices[0] != temp_q[0]:
        temp_q.rotate(-1)
        left += 1
    while indices[0] != temp_q2[0]:
        temp_q2.rotate(1)
        right += 1
    ans += min(left, right)

    if left <= right:
        q.rotate(-left)
        q.popleft()
        indices.popleft()
    else:
        q.rotate(right)
        q.popleft()
        indices.popleft()
print(ans)