import sys
from collections import deque

input = sys.stdin.readline
print = sys.stdout.write

t = int(input())

for _ in range(t):
    function = deque(input().rstrip())
    n = int(input().rstrip())
    arr = input().rstrip()

    is_error = 0
    backward = 0
    q = deque()
    arr = arr[1:-1].split(',') # without brackets
    if arr[0] != '':
        for num in arr:
            q.append(int(num))
    
    while function:
        if function.popleft() == 'R':
            if backward == 0:
                backward = 1
                continue
            else:
                backward = 0
                continue
        else:
            if len(q) == 0:
                print('error\n')
                is_error = 1
                break
            else:
                if backward == 1: q.pop()
                else: q.popleft()
    
    if is_error == 1:
        continue
    else:
        if len(q) == 0:
            print('[]\n')
        else:
            if backward == 0:
                print('[' + ','.join(map(str, q)) + ']\n')
            else:
                q.reverse()
                print('[' + ','.join(map(str, q)) + ']\n')