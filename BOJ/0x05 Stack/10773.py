import sys
from collections import deque
input = sys.stdin.readline

stack = deque()
k = int(input())

for _ in range(k):
    command = int(input())

    if command == 0:
        stack.pop()
    else:
        stack.append(command)
print(sum(stack))