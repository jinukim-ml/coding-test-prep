import sys

n = int(sys.stdin.readline().strip())
arr = [0] * 26
arr2 = [0] * 26
decisions = []
for _ in range(n):
    cnt = 0
    a, b = sys.stdin.readline().strip().split()
    if len(a) != len(b): decisions.append('Impossible')
    else:
        for idx in range(len(a)):
            arr[ord(a[idx])-97] += 1
            arr2[ord(b[idx])-97] += 1
        for i in range(26):
            if arr[i] == arr2[i]: cnt += 1
            arr[i] = 0
            arr2[i] = 0
        if cnt == 26: decisions.append('Possible')
        else: decisions.append('Impossible')

    if cnt == 26: sys.stdout.write('Possible' + '\n')
    else: sys.stdout.write('Impossible' + '\n')
    cnt = 0