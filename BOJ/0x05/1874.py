import sys
from collections import deque
input = sys.stdin.readline
print = sys.stdout.write

n = int(input())
stack = deque()
target = []
arr = []
for _ in range(n):
    target.append(int(input()))

stack.append(1)
index = 0
used = 1
commands = ['+']
while index < len(target):
    if target[index] > used:
        used += 1
        stack.append(used)
        commands.append('+')
    elif len(stack) > 0:
        if target[index] == stack[-1]:
            arr.append(stack.pop())
            index += 1
            commands.append('-')
        elif target[index] < used:
            stack.pop()
            commands.append('-')
    else: break

if len(arr) == len(target):
    for command in commands:
        print(command + '\n')
else:
    print('NO\n')