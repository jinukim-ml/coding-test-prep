import sys
a = []
n = int(sys.stdin.readline())
for x in range(n):
    com, *data = sys.stdin.readline().split()
    
    if com == 'push_front':
        a.insert(0, data[0])
    elif com == 'push_back':
        a.append(data[0])
    elif com == 'pop_front':
        print(a.pop(0) if a else -1)
    elif com == 'pop_back':
        print(a.pop() if a else -1)
    elif com == 'size':
        print(len(a))
    elif com == 'empty':
        print(0 if a else 1)
    elif com == 'front':
        print(a[0] if a else -1)
    elif com == 'back':
        print(a[-1] if a else -1)