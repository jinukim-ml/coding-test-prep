import sys
readline = sys.stdin.readline
write = sys.stdout.write

n = int(readline())
for i in range(1, n+1):
    write(' '*(n-i) + '*'*(2*i-1) + '\n')