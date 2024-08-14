n = int(input())
arr = list(map(int, input().split()))

m = int(input())
targets = list(map(int, input().split()))

book = {}
for i in range(n):
    book[arr[i]] = 1

ans = []
for i in range(m):
    if targets[i] in book:
        ans.append(1)
    else:
        ans.append(0)

for res in ans:
    print(res)