import sys
readline = sys.stdin.readline
write = sys.stdout.write

n = int(readline())
for i in range(n):
    write(' '*i + '*'*(n-i) + '\n')