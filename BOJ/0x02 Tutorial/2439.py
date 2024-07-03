num = int(input())
for x in range(num):
    s = ' '*(num-x-1)+'*'*(x+1)
    print(s)