import sys
readline = sys.stdin.readline
arr = list(map(int, readline().split()))
print(*sorted(arr[::-1]))