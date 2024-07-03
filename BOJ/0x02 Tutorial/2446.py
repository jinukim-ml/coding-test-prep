import sys
readline = sys.stdin.readline
write = sys.stdout.write

n = int(readline())

for i in range(n, 0, -1):
    write(' '*(n-i) + '*'*(2*i-1) + '\n')

for j in range(2, n+1):
    write(' '*(n-j) + '*'*(2*j-1) + '\n')