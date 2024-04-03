from collections import deque

def solution2(maps):
    n, m = len(maps), len(maps[0])
    dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]  # Movement directions (right, left, down, up)

    queue = deque([(0, 0)])  # Start at (0, 0)
    visited = [[False] * m for _ in range(n)]
    visited[0][0] = True

    distance = 1  # Initial distance from starting point
    while queue:
        for _ in range(len(queue)):
            x, y = queue.popleft()

            if x == n - 1 and y == m - 1:  # Reached the opponent's base
                return distance

            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == 1 and not visited[nx][ny]:
                    visited[nx][ny] = True
                    queue.append((nx, ny))

        distance += 1  # Increment distance after each level of exploration

    return -1  # Unreachable if queue becomes empty