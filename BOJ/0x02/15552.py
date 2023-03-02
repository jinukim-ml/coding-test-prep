import sys
t = int(input())
if t > 0 and t <= 1000000:
    for x in range(t):
        a,b = map(int,sys.stdin.readline().split())
        if a >= 1 and a <= 1000 and b >= 1 and b <= 1000:
            print(a+b)