import sys
readline = sys.stdin.readline
write = sys.stdout.write

n = int(readline())
arr = [0, 1, 1]
prev = 1
curr = 1
cnt = 2
if n == 0:
    print(arr[0])
elif n == 1:
    print(arr[1])
elif n == 2:
    print(arr[2])
else:
    while n != cnt:
        next_fib = prev + curr
        prev = curr
        curr = next_fib
        cnt += 1
    print(curr)