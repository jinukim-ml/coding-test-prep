import sys
from collections import deque

q = deque()
input = sys.stdin.readline
print = sys.stdout.write

n = int(input())
for _ in range(n):
    command = input().split()

    if command[0] == 'push':
        q.append(int(command[1]))
    if command[0] == 'pop':
        if len(q) == 0: print('-1\n')
        else: print(str(q.popleft()) +'\n')
    if command[0] == 'size':
        print(str(len(q)) + '\n')
    if command[0] == 'empty':
        if len(q) == 0: print('1\n')
        else: print('0\n')
    if command[0] == 'front':
        if len(q) == 0: print('-1\n')
        else: print(str(q[0]) + '\n')
    if command[0] == 'back':
        if len(q) == 0: print('-1\n')
        else: print(str(q[-1]) + '\n')