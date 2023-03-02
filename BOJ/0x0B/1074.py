import sys

def Z(n, r, c):
    if n == 0: return 0
    else:
        if r <= 2**(n-1)-1 and c <= 2**(n-1)-1:
            return Z(n-1, r, c)
        if r <= 2**(n-1)-1 and c > 2**(n-1)-1:
            return 2**(2*n-2) + Z(n-1, r, c-2**(n-1))
        if r > 2**(n-1)-1 and c <= 2**(n-1)-1:
            return 2**(2*n-1) + Z(n-1, r-2**(n-1), c)
        if r > 2**(n-1)-1 and c > 2**(n-1)-1:
            return 3 * 2**(2*n-2) + Z(n-1, r-2**(n-1), c-2**(n-1))

input = sys.stdin.readline
n, r, c = map(int, input().split())

print(Z(n,r,c))