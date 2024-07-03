import sys
readline = sys.stdin.readline
write = sys.stdout.write

n = int(readline())
for i in range(1, n+1):
    write(' '*(n-i) + '*'*(2*i-1) + '\n')
for i in range(2, n+1):
    write(' '*(i-1) + '*'*(2*n-(2*i-1)) + '\n')