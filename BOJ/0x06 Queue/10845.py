import sys
a = []
n = int(sys.stdin.readline())
for x in range(n):
    com, *data = sys.stdin.readline().split()
    
    if com == 'push':
        a.append(data[0])
    elif com == 'pop':
        print(a.pop(0) if a else -1)
    elif com == 'size':
        print(len(a))
    elif com == 'empty':
        print(0 if a else 1)
    elif com == 'front':
        print(a[0] if a else -1)
    elif com == 'back':
        print(a[-1] if a else -1)