import sys
readline = sys.stdin.readline

arr = []
for _ in range(5):
    arr.append(int(readline()))

print(sum(arr)//5, sorted(arr)[2], sep='\n')