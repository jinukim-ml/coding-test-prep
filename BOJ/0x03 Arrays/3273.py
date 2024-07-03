import sys

n = int(sys.stdin.readline().strip())
arr = list(map(int, sys.stdin.readline().strip().split()))
x = int(sys.stdin.readline().strip())
cnt = 0

numbers = [0]*(1000001)

for idx, num in enumerate(arr):
    numbers[num] += 1

for idx, num in enumerate(arr):
    numbers[num] += 1
    if x-num >= 1000000: continue
    if numbers[x-num] == 1: cnt += 1

print(cnt)