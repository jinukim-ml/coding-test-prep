import sys
readline = sys.stdin.readline

arr = []
for _ in range(7):
    num = int(readline())
    if num%2 == 1:
        arr.append(num)

if len(arr) == 0:
    print('-1')
else:
    print(sum(arr), min(arr), sep='\n')