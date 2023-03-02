import sys
readline = sys.stdin.readline
write = sys.stdout.write

n = int(readline())

for i in range(1, n+1):
    write('*'*i + ' '*(2*n-2*i) + '*'* i + '\n')
for j in range(n-1, 0, -1):
    write('*'*j + ' '*2*(n-j) + '*'*j + '\n')