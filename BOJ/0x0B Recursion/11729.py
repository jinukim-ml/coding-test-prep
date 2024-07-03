import sys

def hanoi(num, start, target):
    if num == 1: print(str(start) + ' ' + str(target))
    else:
        hanoi(num-1, start, 6-start-target)
        print(str(start) + ' ' + str(target))
        hanoi(num-1, 6-start-target, target)

input = sys.stdin.readline
n = int(input().rstrip())

print(str(2**n-1))
hanoi(n, 1, 3)