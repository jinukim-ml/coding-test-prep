import sys

a = int(sys.stdin.readline().strip())
b = int(sys.stdin.readline().strip())
c = int(sys.stdin.readline().strip())

sol = str(a*b*c)
arr = [0] * 10
for idx, num in enumerate(str(sol)):
    arr[int(num)] += 1

for i in range(10):
    print(arr[i])