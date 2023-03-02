import sys
readline = sys.stdin.readline
write = sys.stdout.write

maximum, idx = 0, 0
for i in range(1, 10):
    num = int(readline())
    if num > maximum:
        maximum = num
        idx = i

print(maximum, idx, sep='\n')