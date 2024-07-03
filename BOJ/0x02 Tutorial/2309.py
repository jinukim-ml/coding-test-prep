import sys
a = []
b = []
brk_point = False
for x in range(9):
    a.append(int(sys.stdin.readline()))

for i in range(8):
    b.append(a.pop(i))
    for j in range(i, 8):
        b.append(a.pop(j))
        if sum(a) == 100:
            brk_point = True
            break
        else:
            a.insert(j, b.pop())
    if brk_point == True:
        break
    a.insert(i, b.pop())

for x in sorted(a):
    print(x)