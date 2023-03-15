import sys
readline = sys.stdin.readline
write = sys.stdout.write

n, m = map(int, readline().split())
arr = [0]*10
used = [0]*10

def backtrack(k: int):
    if k == m:
        for i in range(m):
            write(str(arr[i]) + ' ')
        write('\n')
    
    for i in range(1, n+1):
        if used[i] == 0:
            arr[k] = i
            used[i] = 1
            backtrack(k+1)
            used[i] = 0

backtrack(0)