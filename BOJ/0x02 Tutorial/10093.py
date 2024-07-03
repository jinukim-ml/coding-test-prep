a,b = map(int, input().split())
if a > b:
    print(a-b-1)
    for i in range(a-b-1):
        print(b+i+1, end=' ')
if b > a:
    print(b-a-1)
    for i in range(b-a-1):
        print(a+i+1, end=' ')
if a == b:
    print(0)