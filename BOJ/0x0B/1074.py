import sys
input = sys.stdin.readline

def Z(n:int, r:int, c:int):
    assert r >= 0 and c >= 0
    if n == 1:
        return 2*r + c
    else:
        if r < 2**(n-1) and c < 2**(n-1): # Upper left
            return Z(n-1, r, c)
        if r < 2**(n-1) and c >= 2**(n-1): # Upper right
            return 2**(2*n-2) + Z(n-1, r, c - 2**(n-1))
        if r >= 2**(n-1) and c < 2**(n-1): # Bottom left
            return 2**(2*n-1) + Z(n-1, r - 2**(n-1), c)
        if r >= 2**(n-1) and c >= 2**(n-1): # Bottom right
            return 3 * 2**(2*n-2) + Z(n-1, r-2**(n-1), c-2**(n-1))

n, r, c = map(int, input().split())
print(Z(n, r, c))