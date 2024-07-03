import sys
from collections import deque

input = sys.stdin.readline
input()
towers = map(int, input().split())
stack = deque()
receivers = []

for tower_idx, tower in enumerate(towers, 1):
    matched_tower = 0
    while len(stack):
        height, location = stack.pop()

        if height > tower:
            matched_tower = location
            stack.append([height, location])
            break
    
    stack.append([tower, tower_idx])
    receivers.append(matched_tower)

print(' '.join(map(str, receivers)))