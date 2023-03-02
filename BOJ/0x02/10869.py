a,b = map(int,input().split())
if a >= 1 and b >= 1 and a <= 10000 and b <= 1000:
    print("%d\n%d\n%d\n%d\n%d" %((a+b),(a-b),(a*b),(a/b),(a%b)))